word_list = ['hello','world','my','name','is','Anna']
char = 'o'

def findWords(letter, wordList):
    newList = []

    for word in wordList:
        if letter in word:
            newList.append(word)
    return newList

print findWords(char, word_list)
