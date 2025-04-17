import re
import config
import json
from difflib import SequenceMatcher

class TextProcessor:

    '''
    Class handles the text processing and text retreival from selected tokens.
    '''

    def __init__(self):
        self.change_list=[]

    #Get the delta parts and index.
    def get_string_differences(self, original, modified):
        '''
        Get the difference delta between the modified string and original string
        
        Args:
        original : original text
        modified : modified of processed text
        
        Returns:
        the changes between the 2 strings including operations like 'replace', 'delete' and the indexed mapped between oiginal and modified string.
        
        '''

        matcher = SequenceMatcher(None, original, modified)
        opcodes = matcher.get_opcodes()
        changes = []
        
        for tag, i1, i2, j1, j2 in opcodes:
            if tag in {'replace', 'delete', 'insert', 'equal'}:
                change = {
                'type': tag,
                'original_text': original[i1:i2],
                'modified_text': modified[j1:j2],
                'original_indexes': (i1, i2),
                'modified_indexes': (j1, j2)
                }
                changes.append(change)
        
        return changes

    def add_to_change_list(self,change):
        '''
        Add the change to Class variable for future retreival.
        
        Args:
        change : Chnages between the original and modeified.

        '''
        self.change_list.append(change)
    
    def get_reverse_changed_string(self,change):
        '''
        Get the original/previous string from current one using the changed details
        
        Args:
        change : Changes between the current and original/previous string.

        Returns:
        original/previous string

        '''
        reconstructed=[]
        for cur_chng in change:
            if cur_chng['type'] in ['replace', 'delete', 'equal']:
                # For reconstructing original, we take only from original string
                reconstructed.append(cur_chng['original_text'])
                # We skip insertions, since they don't exist in original
        
        return ''.join(reconstructed)
    
    def get_selected_from_reverse_changed_string(self,change,selected):
        '''
        Get the index of original/previous index from the selected part of current string
        
        Args:
        change : Changes between the current and original/previous string.
        selected: selected part index of current string.

        Returns:
        original/previous string mapped to current selected string index.

        '''
        new_selected=[]
        for select in selected:
            updated_index=[]
            for cur_idx in select:
                for cur_chng in change:
                    if cur_chng['type'] in ['replace','equal']:
                        if cur_chng['modified_indexes'][0]<= cur_idx <cur_chng['modified_indexes'][1]:
                            offset = cur_idx - cur_chng['modified_indexes'][0]
                            updated_index.append(cur_chng['original_indexes'][0]+offset)
                            break
                    elif cur_chng['type'] in ['delete']:
                        continue
            
            new_selected.append(updated_index)

        return new_selected 

    

    def get_text_from_change(self,change,selected):
        '''
        Get the text and selected index from current string to original/previous string
        
        Args:
        change : Changes between the current and original/previous string.
        selected: selected part index of current string.

        Returns:
        original/previous string and original/previous string mapped to current selected string index.

        '''
        
        current_string = self.get_reverse_changed_string(change)
        selected = self.get_selected_from_reverse_changed_string(change,selected)
        return current_string,selected


    def get_actual_text(self,selected):
        '''
        Get the actual text list from selected tokens  using the selcted index.
        
        Args:
        selected: selected tokens indexes.

        Returns:
        Returns the list of actual text

        '''
        actual_text_list=[]
        if not selected:
            return []
        
        selected_list=[]
        text=""

        for offst in selected:
            selected_list.append(offst[0])

        for change in reversed(self.change_list):
            text,selected_list =  self.get_text_from_change(change,selected_list)
        
        for select in selected_list:
            if len(select)<2:
                select.append(len(text))
            actual_text_list.append(text[select[0]:select[1]])

        return actual_text_list


    #Remove a subtring from String and find the difference
    def remove_substring(self,text,substring):
        processed_text = text.replace(substring,'')
        string_difference= self.get_string_differences(text,processed_text)
        self.add_to_change_list(string_difference)
        return processed_text, string_difference
    
    #substitute foo for h.*?w and find the difference
    def substitute_using_regex(self,text,regex,replaced_text):
        processed_text =  re.sub(regex, replaced_text, text)
        string_difference = self.get_string_differences(text,processed_text)
        self.add_to_change_list(string_difference)
        return processed_text, string_difference
    
    #Function with pipeline to preprocess.
    def process_text(self,text):
        self.change_list=[]
        custom_tokens = []
        current_text = text

        with open(config.TEXT_PROCESS_JSON) as f:
            process_json = json.load(f)
            for process in process_json:

                if process["type"] == "delete":
                    current_text,string_difference = self.remove_substring(current_text,process["pattern"])

                elif process["type"] == "replace":
                    current_text,string_difference = self.substitute_using_regex(current_text,process["pattern"],process["replace"])
                    custom_tokens.append(process["replace"])


        return current_text,custom_tokens
