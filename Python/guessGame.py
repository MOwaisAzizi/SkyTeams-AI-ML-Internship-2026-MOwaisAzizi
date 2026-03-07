# youtuber = 'ali'
# print("subscript to {}".format(youtuber))

# print(f"subscript to {youtuber}")
# print("subscript to " + youtuber)

# name = input('enter your name')
# age = int(input('how old are you?'))
# job = input('what do you do?')
# data = f"my name is {name} and I am {age} years old and I do ${job}"
# print(data)
import random

# def guessGame(x):
#     randomNumber = random.randint(1, x)
#     guess = 0
#     while(guess != randomNumber):
#         guess = int(input('Please guesss the numberz: '))
#         if(guess > randomNumber):
#             print('too high. please guess lower')
#         if(guess < randomNumber):
#             print('too low. please guess higher')
#     print(f'Congrats. You guessed corrent. {randomNumber}')
# guessGame(10)

def computerGuess(x):
    guess = 0
    low = 1
    high = x
    feedback = ''
    while(feedback != 'c'):
        guess = random.randint(low, high)
    #    if(guess > currectNumber ):
        feedback = input(f'{guess}: Am I high(h). low(l) or correct(c)')
        if(feedback == 'h'):
            high = guess - 1
        elif(feedback == 'l'):
            low = guess + 1

    print('your guess is corrent', guess)

computerGuess(100)

# computerGuess(100)


def playRockPaper():
    userChoise = input('what is your choise: r(rock) paper(p) sessior(s): ')
    computerChose = random.choice(['r', 'p', 's'])
    print(userChoise)
    print(computerChose)
    if userChoise == computerChose:
        print('tie')
        return

    if checkWinner(userChoise, computerChose):
        return print('You win')
    print('you lost')
 
def checkWinner(user, computer):
    if (user=='r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        return True

playRockPaper()
