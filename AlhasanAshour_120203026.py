#DONE BY ALHASAN ASHOUR
#ID : 120203026
#NLP COURSE 
#HW2 : MINIMUM EDIT DISTANCE ASSIGNMENT

import numpy as np

def levenshtein_Count_word(sent1, sent2):
    seq1 = sent1.split()
    seq2 = sent2.split()
    return levenshtein_Count_Char(seq1,seq2)
    
def levenshtein_Count_Char(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros ((size_x, size_y))
    for x in range(size_x):
        matrix [x, 0] = x
    for y in range(size_y):
        matrix [0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            count = 0 \
            if seq1[x-1] == seq2[y-1] else 2
            matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1]+count,
                    matrix[x, y-1] + 1
                )

    print (matrix)
    return (matrix[size_x - 1, size_y - 1])



word1 = "intention"
word2 = "execution"


print("Minimum Edit Distance is %s"%levenshtein_Count_Char(word1,word2))

sent1 = "WELCOME TO NLP COURSE"
sent2 = "TESTING MINIMUM EDIT DISTANCE TO COUNT WORDS IN SENTENCES"

print("############################################")
print(sent1)

print("############################################")
print(sent2)

print("############################################")
print("Minimum Edit Distance is %s"%levenshtein_Count_word(sent1,sent2))

print("############################################")
print("#DONE BY ALHASAN ASHOUR \n #ID : 120203026 \n  #NLP COURSE  \n  #HW2 : MINIMUM EDIT DISTANCE ASSIGNMENT")