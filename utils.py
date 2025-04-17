def merge_offset(intervals):
    '''
    Get the merged index of the selected tokens which are close to each other

    args:
    intervals :  intervals of the selected tokens

    Returns:
    Returns the merged indexed of overlapping indexes.
    '''
    if not intervals:
        return []
    first = intervals[0]
    last = intervals[-1]
    merged = [(first[0],last[1])]
    return merged



def get_selected_token_and_offset(tokens,offset_mapping,classification_result):
    '''
    Get the selected tokens using the classification results.

    args:
    tokens :  tokens list
    offset_mapping : get the mapping between tokens and string that is tokenized.
    classification_result : The results of the classification results.

    Returns:
    selected tokens and there index using classification results.
    
    '''
    selected_tokens=[]
    selected_offset=[]
    current_token=[]
    current_offset=[]
    for idx,cls in enumerate(classification_result):
        if cls==0:
            if len(current_token)>0:
                selected_tokens.append(current_token)
                selected_offset.append(current_offset)
            current_token=[]
            current_offset=[]
        else:
            current_token.append(tokens[idx])
            current_offset.append(offset_mapping[idx])
    if len(current_token)>0:
        selected_tokens.append(current_token)
        selected_offset.append(current_offset)

    selected_offset_merged=[]
    for offset in selected_offset:
        selected_offset_merged.append(merge_offset(offset))

    
    return selected_tokens,selected_offset_merged
