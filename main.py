from text_classifier_and_retreiver import TextClassifierAndRetreiver

#Flag to run or test code.
TEST_CODE = False

#Run the code.
def run():
    #Run text to get results
    run_samples = [
        "hello world how how how are you?",
        "hi how are you",
        "On this wondrous world, voices of hope, joy, and devotion echo boldly through the horizon."
    ]


   
    #Initialize the text classifier and retreiver class
    textClassifierAndRetreiver = TextClassifierAndRetreiver()
    print("Intilialized TextClassifierAndRetreiver....")


    for text in run_samples:
        #Pass the test as argumen and get
        # processed_text: Preprocessed text 
        #tokens: Tokenized tokens
        #classification_result : Classification labels of the model
        #selected_text_list : List of text of the selected tokens.
        #actual_text_list : List of the actual text of selected tokens.

        processed_text,tokens,classification_result,selected_text_list,actual_text_list = textClassifierAndRetreiver.classify_and_retreive(text)

        print("Original Text : ", text)
        print("Processed Text : ", processed_text)
        print("Tokens : ",tokens)
        print("Classification Label : ", classification_result)
        print("Selected Token : ", selected_text_list)
        print("Actual Text :", actual_text_list)
        print("############################################################")
        

#Testing the application.
def test():
    
    print("Testing code.")

    test_good_samples = [
        ["how does this system handle unexpected inputs?",[0, 0, 0, 0, 0, 1, 0, 1, 0],['unexpected', 's']],
        ["however, the results varied significantly across different test cases.", [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],['ever, the results', 'different test', '.']],
        ["how can we improve the model's accuracy without increasing latency?",[1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],['how', 'we imp', 'hout', '?']],
        ["however you approach the problem, consistency is key.",[1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],['how', 'u', 'problem', 'isten', '.']],
        ["how it works depends on the configuration you choose.",[1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1],['how it', 'rks', 's on the', 'figuration you', '.']]

    ]

    test_bad_samples = [
        ["how does this system handle unexpected inputs?",[0, 0, 1, 0, 0, 1, 0, 1, 0],['unexpected', 's']],
        ["however, the results varied significantly across different test cases.", [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],['ever, the results', 'different test', '.']],
        ["how can we improve the model's accuracy without increasing latency?",[1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1],['how', 'we imp', 'hout', '?']],
        ["however you approach the problem, consistency is key.",[1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],['how', 'u', 'problem', 'isten', '.']],
        ["how it works depends on the configuration you choose.",[1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1],['how it', 'rks', 's on the', 'figuration you', '.']]

    ]
     
    #Initialize the text classifier and retreiver class
    textClassifierAndRetreiver = TextClassifierAndRetreiver()
    print("Intilialized TextClassifierAndRetreiver....")

    print("Good Test")
    print("=============")
    #Test good test
    for test in test_good_samples:
        #Pass the test as argumen and get
        # processed_text: Preprocessed text 
        #tokens: Tokenized tokens
        #classification_result : Classification labels of the model
        #selected_text_list : List of text of the selected tokens.
        #actual_text_list : List of the actual text of selected tokens.

        processed_text,tokens,classification_result,selected_text_list,actual_text_list = textClassifierAndRetreiver.classify_and_retreive(test[0],test[1])

        print("Return Value :", actual_text_list)
        print("ACompare Value :",test[2])

        assert actual_text_list == test[2]
        print("✅ Assertion good test passed: Result is OK.")
        print("############################################################")
    
    print("Bad Test")
    print("=============")
    #Test bad test
    for test in test_bad_samples:
        #Pass the test as argumen and get
        # processed_text: Preprocessed text 
        #tokens: Tokenized tokens
        #classification_result : Classification labels of the model
        #selected_text_list : List of text of the selected tokens.
        #actual_text_list : List of the actual text of selected tokens.

        processed_text,tokens,classification_result,selected_text_list,actual_text_list = textClassifierAndRetreiver.classify_and_retreive(test[0],test[1])
        
        print("Return Value :", actual_text_list)
        print("Compare Value :",test[2])

        assert actual_text_list != test[2]
        print("✅ Assertion bad test passed: Result is OK.")

        print("############################################################")
        


if __name__ == "__main__":

    if TEST_CODE:
        test()
    else:
        run()


    

    


    


