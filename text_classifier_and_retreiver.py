from text_tokenizer import TextTokenizer
from token_classifier import Classiffier
from text_processor import TextProcessor
from utils import *

class TextClassifierAndRetreiver:
    '''
    Class handles all the steps 1. Processing 2. Tokenization 3. Classification and 4. Retreival of original string of the selected tokens
    
    '''
    def __init__(self):
        '''
        Initialize all necessary class instances.
        '''
        self.textProcessor = TextProcessor()
        self.tokenizer = TextTokenizer()
        self.classifier = Classiffier()

    def classify_and_retreive(self,text,classification_result=[]):
        '''
        Taken in text do the 1. Processing 2. Tokenization 3. Classification and 4. Retreival

        args:
        text :  input text
        classification_result : This will be used for testing.

        Returns:
        processed_text: Preprocessed text 
        tokens: Tokenized tokens
        classification_result : Classification labels of the model
        selected_text_list : List of text of the selected tokens.
        actual_text_list : List of the actual text of selected tokens.

        '''
        
        processed_text,custom_tokens = self.textProcessor.process_text(text)

        self.tokenizer.add_custom_tokens(custom_tokens)
        tokenize_map = self.tokenizer.tokenize_with_offset_mapping(processed_text)
        offset_mapping = tokenize_map['offset_mapping']
        tokens = self.tokenizer.convert_ids_to_tokens(tokenize_map['input_ids'])

        #For testing.
        if len(classification_result)==0:
            classification_result = self.classifier.classifiy(tokens)

        selected_tokens,selected_offsets = get_selected_token_and_offset(tokens,offset_mapping,classification_result)

        selected_text_list=[]
        for selected_token in selected_tokens:
            selected_text_list.append(self.tokenizer.decode(self.tokenizer.convert_tokens_to_ids(selected_token)))

        actual_text_list = self.textProcessor.get_actual_text(selected_offsets)

        return processed_text,tokens,classification_result,selected_text_list,actual_text_list




