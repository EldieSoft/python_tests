import random

def compInput():
    x = random.randint(1,3)
    
    match x:
        case 1:
            return "R"
        case 2:
            return "P"
        case 3:
            return "S"
def compare(player_input, comp_input):
    #Player Wins
    if player_input == "R" and comp_input == "S":
        print("Player Wins!!")
    elif player_input == "S" and comp_input == "P":
        print("Player Wins!!")
    elif player_input == "P" and comp_input == "R":
        print("Player Wins!!")
    #Computer Wins
    elif player_input == "R" and comp_input == "P":
        print("Computer Wins!!")
    elif player_input == "P" and comp_input == "S":
        print("Computer Wins!!")
    elif player_input == "S" and comp_input == "R":
        print("Computer Wins!!")
    #Tie
    elif player_input == "R" and comp_input == "R":
        print("Tie!!")
    elif player_input == "S" and comp_input == "S":
        print("Tie!!")
    elif player_input == "P" and comp_input == "P":
        print("Tie")

print("R for rock, P for paper, S for scissors")

player_input = input()
comp_input = compInput()

if (player_input == "R" or player_input == "S" or player_input == "P"):
    print("Computer Chooses", comp_input)
    compare(player_input, comp_input)
else:
    print("Invalid Input")
