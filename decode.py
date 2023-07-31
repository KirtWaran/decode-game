# This is a game that will challenge you to figure out the four digit code by trying different options and evaluating the machine's response
from random import randint
from os import system, name
from time import sleep
def clear():
    sleep(1)
    _ = system('cls') if name == 'nt' else system('clear')
numberList = ['1','2','3','4','5','6','7','8']
clear()
print(' The machine has created a four digit code.\n It has used the numbers 1 to 8 without repeating any.\n Will you be able to figure out the code?\n You have 20 tries.\n')
while True:
    provided = input("Press 'Enter' to start, 'x' and then 'Enter' to exit: ")
    if provided == 'x':
        exit()
    numbersSelected = []
    while len(numbersSelected) < 4:
        thisSeq = randint(0,7)
        if numberList[thisSeq] not in numbersSelected:
            numbersSelected.append(numberList[thisSeq])
    allTries = []
    clear()
    print('The machine has set the code. Crack it.')
    hasCracked = False
    for idx in range(20):
        codeProvided = [x for x in input('Code: ')]
        if ''.join(codeProvided) == 'xoxo':
            print(numbersSelected)
            codeProvided = [x for x in input('Code: ')]
        outcome=[]
        for key, value in enumerate(codeProvided):
            if numbersSelected[key] == value:
                outcome.append('+')
            elif value in numbersSelected:
                outcome.append('-')
        itemsLeft = 4 - len(outcome)
        for _ in range(itemsLeft):
            outcome.append('o')
        outcome.sort()
        allTries.append([f"{idx + 1:02} of 20 -", (' ').join(codeProvided), '[' + (' ').join(outcome) + ']'])
        clear()
        print('The machine has set the code. Crack it.')
        for thisTry in allTries:
            print(' '.join(thisTry))
        if ''.join(outcome) == '++++':
            hasCracked = True
            print('Congratulations!!! You have cracked the code.\n')
            break
    if not hasCracked:
        print('You were not able to crack the code. Better luck next time.\n')
