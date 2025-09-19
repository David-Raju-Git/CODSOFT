import random

def display_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_win(board, mark):
    combos = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(board[i]==board[j]==board[k]==mark for i,j,k in combos)

def available_moves(board):
    return [i for i in range(9) if board[i] == ' ']

def ai_move(board):
    moves = available_moves(board)
    return random.choice(moves)

def main():
    board = [' ']*9
    print("TIC TAC TOE (Positions: 1-9)")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print("\nYou: X, Computer: O")

    while True:
        display_board(board)
        try:
            pos = int(input("Enter your move (1-9): "))
            idx = pos - 1
            if pos < 1 or pos > 9 or board[idx] != ' ':
                print("Invalid move.")
                continue
            board[idx] = 'X'
            if check_win(board, 'X'):
                display_board(board)
                print("You win!")
                break
            if ' ' not in board:
                display_board(board)
                print("Tie!")
                break
            print("Computer's move...")
            ai_idx = ai_move(board)
            board[ai_idx] = 'O'
            if check_win(board, 'O'):
                display_board(board)
                print("Computer wins!")
                break
            if ' ' not in board:
                display_board(board)
                print("Tie!")
                break
        except:
            print("Enter a valid number from 1 to 9.")
            continue

if __name__ == "__main__":
    main()