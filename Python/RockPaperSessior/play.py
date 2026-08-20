import random

def playRockPaper():
    userChoise = input('what is your choise: r(rock) paper(p) sessior(s): ')
    computerChose = random.choice(['r', 'p', 's'])
    print('you choosed: '+userChoise)
    print('computer choosed: '+computerChose)
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
