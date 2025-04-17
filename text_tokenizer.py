from transformers import AutoTokenizer, AutoModelForMaskedLM

class TextTokenizer:
    """
    Used to tokenize text. Convert to token and ids and vice versa.

    """

    def __init__(self, model_name='xlm-roberta-large'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    def tokenize(self, text):
        """
        Tokenize text
        
        Args:
        text : text to tokenize
        
        Returns:
        tokenized list
        
        """
        return self.tokenizer.tokenize(text)
    
    def tokenize_with_offset_mapping(self, text):
        """
        Tokenize text and get the offset mapping that links text to token
        
        Args:
        text : text to tokenize
        return_offsets_mapping : Get the map between text and tokens
        add_special_tokens :  avoid special tokens.
        
        Returns:
        tokenized list and get the map between text and tokens.
        
        """
        return self.tokenizer(text, return_offsets_mapping=True,add_special_tokens=False)

    
    def convert_tokens_to_ids(self,tokens):
        """
        Convert Token to ids
        
        Args:
        tokens : tokens list to convert
        
        Returns:
        id list
        
        """
        return self.tokenizer.convert_tokens_to_ids(tokens)
    
    def convert_ids_to_tokens(self,ids):
        """
        Convert ids to tokens
        
        Args:
        ids : ids list to convert
        
        Returns:
        token list
        
        """
        return self.tokenizer.convert_ids_to_tokens(ids)

    
    def decode(self, token_ids, skip_special_tokens=True):
        """
        converts token IDs back into a human-readable string

        Args:
        token_ids : ids list to convert
        skip_special_tokens : To skip the special tokens
        
        Returns:
        string token list

        """
        return self.tokenizer.decode(token_ids, skip_special_tokens=skip_special_tokens)
    
    def add_custom_tokens(self,custom_tokens):
        """
        Add custom tokens to tokenizer to avoid them splitting in to multiple tokens.
        
        Args:
        custom_tokens : custom tokens nee to be added
        
        """
        if len(custom_tokens)>0:
            self.tokenizer.add_tokens(custom_tokens)