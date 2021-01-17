import random

p = ['rock', 'paper', 'scissors','lizard', 'spock']
player = False
computer = random.choice(p)

while player == False:
    print('The game is on. Rock, paper, scissors...which one will you choose?')
    player = input()
    if computer == player:
        print('It is a tie!')
    elif player == 'rock':
        if computer == 'paper':
            print('You lose, %s crushes %s'%(computer, player))
        elif computer == 'lizard':
            print('You win!, %s crushes %s'%(player, computer))
        elif computer == 'spock':
            print('You lose, %s vaporizes %s'%(computer, player))
        else:
            print('You win! %s crushes %s'%(player, computer))
    elif player == 'paper':
        if computer =='rock':
            print('You win! %s beats %s'%(player, computer))
        elif computer == 'lizard':
            print('You lose, %s eats %s'%(computer, player))
        elif computer == 'spock':
            print('You win! %s disproves %s'%(player, computer))
        else:
            print('You lose, %s cuts %s'(computer, player))   
    elif player == 'scissors':
        if computer == 'rock':
            print('You lose, %s crushes %s'%(computer, player))
        elif computer == 'lizard':
            print('You win! %s decapitates %s'%(player, computer))
        elif computer == 'spock':
            print('You lose, %s smashes %s'%(computer, player))
        else:
            print('You win! %s cuts %s'%(player, computer))
    elif player == 'lizard':
        if computer == 'rock':
            print('You lose, %s crushes %s'%(computer, player))
        elif computer == 'paper':
            print('You win! %s eats %s'%(player, computer))
        elif computer == 'scissors':
            print('You lose, %s decapitates %s'%(computer, player))
        else:
            print('You win! %s poisons %s'%(player, computer))
    elif player == 'spock':
        if computer == 'rock':
            print('You win %s vaporizes %s'%(player, computer))
        elif computer == 'paper':
            print('You lose, %s disproves %s'%(computer, player))
        elif computer == 'scissors':
            print('You win %s destroys %s'%( player, player))
        else:
            print('You lose, %s poisons %s'%(computer, player))
    else:
        print('Your input is invalid, try one of these instead:'+ str(p))
    player = False
computer = random.choice(p)


  
