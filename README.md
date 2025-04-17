# Task
This repository demonstrates a method for mapping selected tokens back to their original string form after undergoing preprocessing, tokenization, and classification. It includes logic for selecting random tokens and tracing them to their source text. Example of the complete pipeline can be seen below.

```
Original Text :  hello world how how how are you?
Processed Text :  foorld foo foo foo are yu?
Tokens :  ['foo', '▁r', 'ld', 'foo', 'foo', 'foo', '▁are', '▁y', 'u', '?']
Classification Label :  [0, 1, 0, 0, 0, 1, 1, 0, 1, 1]
Selected Token :  ['r', 'foo are', 'u?']
Actual Text : ['r', 'how are', 'u?']

```

# Approach
This section provides a step-by-step breakdown of the methodology used to accomplish the task. The approach consists of four main steps: (1) text preprocessing, (2) tokenization, (3) token classification, and (4) retrieval of sub-strings corresponding to selected tokens. The following sections provide a detailed explanation of each step.  
## Text Preprocessing  
The text preprocessing supports two actions: delete and replace, defined in text_process_config.json (path set via TEXT_PROCESS_JSON in config.py). Changes before and after processing are tracked using difflib.SequenceMatcher, storing details like type, text, and index ranges in self.change_list. These are later used for text retrieval. The TextProcessor class (in text_processor.py) reads the config and applies processing based on metadata.  
![image](https://github.com/user-attachments/assets/28c902f8-f9fe-4d75-a0de-33bdac039b58)
## Tokenization  
This step tokenizes the preprocessed text using Hugging Face’s xlm-roberta-large with return_offsets_mapping=True to map tokens to text positions, and add_special_tokens=False to simplify processing. Tokens introduced during preprocessing are added as special tokens using add_tokens() to prevent splitting. The TextTokenizer class (text_tokenizer.py) manages tokenization and retrieves original substrings for each token. An example output is shown below.
```
Processed Text :  foorld foo foo foo are yu?
Tokens :  ['foo', '_r', 'ld', 'foo', 'foo', 'foo', '_are', '_y', 'u', '?']
```
## Token Classification  
A mock classifier randomly assigns 0s and 1s to tokens. Tokens labeled with 1 are selected; adjacent 1s are merged into spans. Example:
```
Tokens :  ['foo', '_r', 'ld', 'foo', 'foo', 'foo', '_are', '_y', 'u', '?']
Classification Label :  [0, 1, 1, 0, 0, 1, 1, 1, 0, 0]
Selected Token :  ['rld', 'foo are y']
```
The Classifier class (token_classifier.py) handles this logic, producing mock labels matching the token list length.

## Retreival
This step retrieves the original text for selected tokens by reversing stored preprocessing changes. Using self.change_list, the TextProcessor class (text_processor.py) maps selected spans from the processed string back to their original input positions. This is done iteratively through functions like get_reverse_changed_string() and get_selected_from_reverse_changed_string(), which reconstruct previous string states and update token indices. Example of change map can be seen below  
```
[{'type': 'equal', 'original_text': 'On t', 'modified_text': 'On t', 'original_indexes': (0, 4), 'modified_indexes': (0, 4)}, {'type': 'replace', 'original_text': 'his w', 'modified_text': 'foo', 'original_indexes': (4, 9), 'modified_indexes': (4, 7)}, {'type': 'equal', 'original_text': 'ndrus wrld, vices f hpe, jy, and devtin ech bldly thrugh the hrizn.', 'modified_text': 'ndrus wrld, vices f hpe, jy, and devtin ech bldly thrugh the hrizn.', 'original_indexes': (9, 76), 'modified_indexes': (7, 74)}]
```
## Complete Pipeline
This section describes the full pipeline. The original text is preprocessed, tokenized, and classified to identify selected tokens. Using saved transformation history, these tokens are mapped back to their original substrings. The TextClassifierAndRetriever class (text_classifier_and_retriever.py) manages this flow by initializing TextProcessor, TextTokenizer, and Classifier. Use classify_and_retrieve(text) to run the pipeline and get detailed outputs.  

# How to Use
Define the preprocessing steps along with their required parameters in the text_process_config.json file. Then, create an instance of the TextClassifierAndRetriever class and call the classify_and_retrieve(text) method with the input text. A sample code snippet is provided below.
```
textClassifierAndRetreiver = TextClassifierAndRetreiver()
#Pass the test as argumen and get
# processed_text: Preprocessed text 
#tokens: Tokenized tokens
#classification_result : Classification labels of the model
#selected_text_list : List of text of the selected tokens.
#actual_text_list : List of the actual text of selected tokens.
processed_text,tokens,classification_result,selected_text_list,actual_text_list = textClassifierAndRetreiver.classify_and_retreive(text)
```
You can refer to main.py on how to use the run() and test() functions. Use the TEST_CODE flag to switch between the two modes.





