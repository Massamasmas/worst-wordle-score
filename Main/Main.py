'''
i need this program to check every
letter in each valid guess, for every word
that could be the answer.

Thats checking 10657 words
2315 times (24,670,955 checks).
At least they're all the same
word length; i dont gotta deal with extremely
long words.

this only calculates the value of each guess
as the first guess for the given answer


okay, basic algo:
needs a nested for loop in another for loop.
the outermost one will go for the length of answersList,
and the embedded one will go for the length of validguesslist.

that second for loop will have another for loop;
for length of validGuessList[index1],
check if validGuessList[index1][index2]
is in answersList[index1]. if it is, score += 1

(12/5/25 maybe i could use a bult in method for this? let me research that.
i can use the .find method, and if it returns -1 that means that letter isn't
in the word)

if validGuessList[index1][index2] is also in
the same place, score += 10

this saves a word, and it's associated score
given the current answer
scoresList.append [validGuessList[index1], score, answer]

so far this algo will only check the score of
any given guess for each correct answer,
but not the optimally worst selection of guesses.
it doesn't take into account that you
cannot type the same letter again after using it
if it was incorrect.
'''

from AnswersList import answersList1

from AnswersList import answersList2

from AnswersList import answersList3


from ValidGuessList import validGuessList1
from ValidGuessList import validGuessList2
from ValidGuessList import validGuessList3
from ValidGuessList import validGuessList4
from ValidGuessList import validGuessList5
from ValidGuessList import validGuessList6
from ValidGuessList import validGuessList7
from ValidGuessList import validGuessList8
from ValidGuessList import validGuessList9
from ValidGuessList import validGuessList10
from ValidGuessList import validGuessList11



def getLetters(word):
    out = []
    wordLength = len(word)
    for j in range(wordLength):
        out += word[j]
    return(out)
    
'''
precons: gWord and aWord are strings
of the same length. Score is 500

postcons:
returns a score value based on how many letters
aWord and gWord share and how many letters are
at the same index

if the inputs are the same word, the score is set to 0

for each letter that is the same at the same index, the
score is reduced by 100

for each letter that is shared between the words(but not at
the same index) the score is reduced by 20
'''
def checkLetters(gWord, aWord):
    gLetters = getLetters(gWord)
    aLetters = getLetters(aWord)
    score = 500

    if gWord == aWord:
        score = 0
        return(score)
    else:
        for i in range(len(aLetters)):
            if aLetters[i] == gLetters[i]:
                score -= 100
            
            elif gLetters[i] in aWord:
                score -= 20
    
        
    return(score)
    



def main():
    pass


main()