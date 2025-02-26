# Rock, scissors, paper. The Game.
import random
def computer_choice():
    dice = random.randint(1,3)
    if dice == 1:
        return 'Rock'
    elif dice == 2:
        return 'Scissors'
    elif dice == 3:
        return 'Paper'
        
        
def player_choice():
    player_choice = check_number(input)
    if player_choice == 1:
        return 'Rock'
    elif player_choice == 2:
        return 'Scissors'
    elif player_choice == 3:
        return 'Paper'
        

def check_number(num):
    while True:
        try:
            num = int(input("Enter your figure: \n1 - Rock \n2 - Scissors \n3 - Paper "))
        except ValueError:
            print("Please enter a valid number 1-3")
            continue
        if num >= 1 and num <= 3:
            return num
            break
        else:
            print("Please enter a valid number 1-3")
            
    
def fight(comp,player):
    if comp == 'Rock' and player == 'Rock':
        return "Draw"
    elif comp == 'Scissors' and player == 'Scissors':
        return "Draw"
    elif comp == 'Paper' and player == 'Paper':
        return "Draw"
    elif comp == 'Rock' and player == 'Scissors':
        return "Computer win"
    elif comp == 'Scissors' and player == 'Paper':
        return "Computer win"
    elif comp == 'Paper' and player == 'Rock':
        return "Computer win"
    elif player == 'Rock' and comp == 'Scissors':
        return "Meat bag win"
    elif player == 'Scissors' and comp == 'Paper':
        return "Meat bag win"
    elif player == 'Paper' and comp == 'Rock':
        return "Meat bag win"


comp = computer_choice()
player = player_choice()
result = fight(comp,player)

print(f"Player hand - {player}, Computer hand - {comp}, \n{result}")

