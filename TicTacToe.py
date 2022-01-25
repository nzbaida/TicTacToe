#import libraries
import random
import numpy as np

#global constants 
X = "X"
O = "O"
EMPTY = ""
TIE = "TIE"
NUM_POSITIONS = 9
board = [[0,1,2],[3,4,5],[6,7,8]]

#function definitions
#print rules of game
def game_guide():
    print("The goal is to connect 3 of the same symbol vertically, horizontally, or along a diagonal.")
    print("The game board consists of 9 open spaces.")
    print("You, as the player will mark spots on the board with X's.")
    print("Your computer opponent will mark spots on the board with O's.")
    print("Spots on the board are marked 0 through 8.")
    print("You, the player, and the computer will take turns selecting spots on the board by entering a number from 0 to 8")
    print("Once a spot has been filled by you or the computer, it cannot be changed.")
    print("The game ends when you or the computer fill 3 spots along a vertical, horizontal, or diagonal line along the board or when the board is filled and there is no winner, resulting in a tie.")
    print("\n")

#asks user a yes or no question and returns user response
def ask_yes_or_no(question):
    print(question, "Please answer with yes or no.")
    answer = input().lower()
    while answer not in ["yes", "no"]:
        print("Please answer with yes or no")
        answer = input()       
    return answer

#returns an integer value in a range
def ask_number(question, low, high):
    print(question)
    player_answer = int(input())
    while player_answer not in np.arange(low,(high+1),1):
        print("Invalid input")
        player_answer = int(input())
    output = random.randint(low,high)
    if abs(output - player_answer) < 2:
        output -= 1
    return output

#keeping track of pieces as either human or computer
def game_piece(turn):
    player_piece = X
    computer_piece = O
    if turn == "player":
        return player_piece
    elif turn == "computer":
        return computer_piece

#clears the board
def empty_board():
    global board 
    board = [[0,1,2],[3,4,5],[6,7,8]]

#returns the current state of the board
def display_board(board):
    print(board[0])
    print(board[1])
    print(board[2])
    print("\n")

#returns possible moves
def allowed_moves(board):
    possible = []
    for i in [0,1,2]:
        for j in [0,1,2]:
            if board[i][j] != X and board[i][j] != O:
                possible.append(board[i][j])
    return possible

#returns the winner of the game
def winner(board):
    computer = "computer"
    player = "player"
    if board[0][0] == board[0][1] == board[0][1] == X:
        return player
    elif board[1][0] == board[1][1] == board[1][2] == X:
        return player
    elif board[2][0] == board[2][1] == board[2][2] == X:
        return player
    elif board[0][0] == board[1][0] == board[2][0] == X:
        return player
    elif board[0][1] == board[1][1] == board[2][1] == X:
        return player
    elif board[0][2] == board[1][2] == board[2][2] == X:
        return player
    elif board[0][0] == board[1][1] == board[2][2] == X:
        return player
    elif board[0][2] == board[1][1] == board[2][0] == X:
        return player

    if board[0][0] == board[0][1] == board[0][1] == O:
        return computer
    elif board[1][0] == board[1][1] == board[1][2] == O:
        return computer
    elif board[2][0] == board[2][1] == board[2][2] == O:
        return computer
    elif board[0][0] == board[1][0] == board[2][0] == O:
        return computer
    elif board[0][1] == board[1][1] == board[2][1] == O:
        return computer
    elif board[0][2] == board[1][2] == board[2][2] == O:
        return computer
    elif board[0][0] == board[1][1] == board[2][2] == O:
        return computer
    elif board[0][2] == board[1][1] == board[2][0] == O:
        return computer

    elif len(allowed_moves(board)) == 0:
        return TIE
    
#human move
def player_move(board, turn = "player"):
    print("Player, place a piece on the board.")
    move = int(input())
    while move not in allowed_moves(board):
        print("Invalid input.")
        move = input()
    if move >= 0 and move <= 2:
        board[0][move] = game_piece(turn)
    elif move >= 3 and move <= 5:
        board[1][move - 3] = game_piece(turn)
    elif move >= 6 and move <= 8:
        board[2][move - 6] = game_piece(turn)
    
#computer move
def computer_move(board,guess, turn = "computer"):
    move = int(guess)
    while move not in allowed_moves(board):
        move = random.randint(0,8)
    if move >= 0 and move <= 2:
        board[0][move] = game_piece(turn)
    elif move >= 3 and move <= 5:
        board[1][move - 3] = game_piece(turn)
    elif move >= 6 and move <= 8:
        board[2][move - 6] = game_piece(turn)

#swaps turns
def next_turn():
    global turn
    if turn == "computer":
        turn = "player"
    elif turn == "player":
        turn = "computer"

#announces winner
def announce_winner(board):
    return winner(board)

#main
game_guide()
q1 = "Is dumpling the cutest?"
answer = ask_yes_or_no(q1)
if answer == "yes":
    turn = "player"
else:
    turn = "computer"
display_board(board)
while True:
    if turn == "player":
        player_move(board)
    elif turn == "computer":
        q2 = "Guess a number between 0 and 8."
        guess = ask_number(q2,0,8)
        computer_move(board,guess)
    display_board(board)
    next_turn()
    who_won = winner(board)
    if who_won in ["computer", "player", TIE]:
        break
print("The winner is:", announce_winner(board))
print("Thank you for playing!")
print("\n")

