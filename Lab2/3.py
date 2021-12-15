filePath = "lab3_test_data.txt"

def countElements(filePath):
    with open(filePath, 'r') as file:
        linesAmount = 0
        wordsAmount = 0
        lettersAmount = 0
        for line in file:
            linesAmount += 1
            
            words = line.split()
            wordsAmount += len(words)
            
            for word in words:
                lettersAmount += len(word)
            
        print("Lines: ", linesAmount)
        print("Words: ", wordsAmount)
        print("Letters: ", lettersAmount)
        
countElements(filePath)