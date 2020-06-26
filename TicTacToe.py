#Python 3.7.6 | 26.06.2020
#scalable tictactoe based on Santdex youtube series | https://youtu.be/eXBD2bB9-RA
#recreated by github.com/AnyCharacter

from itertools import cycle

def win(current_game):
    
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
        
    #Horizontal
    for row in game:
        if all_same(row):
            print(f'Player {row[0]} is the winner horizontally!')
            return True
    #Diagonal Right to left
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f'Player {diags[0]} is the winner diagonally! (RL) ')
        return True
    #Diagonal Left to right
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f'Player {diags[0]} is the winner diagonally! (LR)')
        return True
        
    #Vertical
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])   
        if all_same(check):
            print(f'Player {check[0]} is the winner vertically!')
            return True
    
    return False
        
        
def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is occupado! Choose another!")
            return game_map, False
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:   
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)    
        return game_map, True 
    except IndexError:
        print("Error: make sure you input row/column as 0, 1 or 2")
        return False
    except Exception:
        print("Oops! Something went wrong. Error!")
        return False
        
play= True
players = [1,2]
while play:
    game_size = int(input("What size game of tic tac toe? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = cycle([1,2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        played = False  
        while not played:
            try:
                column_choice = int(input("What column do you want to play? (0,1,2 etc): "))
                row_choice = int(input("What row do you want to play? (0,1,2 etc): "))
                game, played = game_board(game, current_player, row_choice, column_choice)
            except Exception:
                continue     

        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n) ")
           
            if again.lower() == "y":
                print("restarting")
            elif again.lower() == "n":
                print("Thanks for playing!")
                play = False
            else:
                print('Cup of tea then?')
                play = False        