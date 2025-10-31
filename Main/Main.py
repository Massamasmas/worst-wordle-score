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

that second for loop will have another,
for length of validGuessList[index1],
check if validGuessList[index1][index2]
is in answersList[index1]. if it is, score += 1

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
from AnswersList import answersListTL

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
from ValidGuessList import validGuessListTL

