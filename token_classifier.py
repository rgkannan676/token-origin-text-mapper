#This class is a classification model result emulator
import random

class Classiffier:
    '''
    Get the class mocks a clssification model using length of token
    
    '''
    def classifiy(self, tokenList):
        '''
        Returns a randomly generated list mocking classification model

        args:
        tokenList : token list to get the len of tokens

        Returns:
        Retuns a list or random 1's and 0's of size equal to token length.
        
        
        '''
        token_len = len(tokenList)
        return [random.choice([0,1]) for _ in range(token_len)]