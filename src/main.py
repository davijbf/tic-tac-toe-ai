import os

SIZE = 9

board = [' ' for _ in range(SIZE)]

def clear_cli():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board():
    clear_cli()
    print(
    f"\n3  {board[0]} | {board[1]} | {board[2]}\n" \
    "  -----------\n" \
    f"2  {board[3]} | {board[4]} | {board[5]}\n" \
    "  -----------\n" \
    f"1  {board[6]} | {board[7]} | {board[8]}\n" \
    "   a   b   c\n")

def check_winner(board):
    for i in range(0, 9, 3):
        if board[i] != ' ' and board[i] == board[i+1] == board[i+2]:
            if board[i] == 'X': return 'X'
            else: return 'O'
    for i in range(3):
        if board[i] != ' ' and board[i] == board[i+3] == board[i+6]:
            if board[i] == 'X': return 'X'
            else: return 'O'
    if board[0] != ' ' and board[0] == board[4] == board[8]:
        if board[0] == 'X': return 'X'
        else: return 'O'  
    if board[2] != ' ' and board[2] == board[4] == board[6]:
        if board[2] == 'X': return 'X'
        else: return 'O'
    return None
    
def available_moves(board):
    moves = []
    for i in range(SIZE):
        if board[i] == ' ': moves.append(i)
    return moves

def minmax(board, is_max):
    result = check_winner(board)
    if result == 'X': return 1
    elif result == 'O': return -1
    available = available_moves(board)
    if not available: return 0
    if is_max:
        best_score = -2
        for i in available:
            board[i] = 'X'
            best_score = max(minmax(board, False), best_score)
            board[i] = ' '     
    else:
        best_score = 2
        for i in available:
            board[i] = 'O'
            best_score = min(minmax(board, True), best_score)
            board[i] = ' '
    return best_score
    
def bot_move(board, turn):
    available = available_moves(board)
    if turn == 'X':
        best_score = -2
        best_move = -1
        for i in available:
            board[i] = 'X'
            test = minmax(board, False)
            if test > best_score:
                best_score = test
                best_move = i
            board[i] = ' '
    else:
        best_score = 2
        best_move = -1
        for i in available:
            board[i] = 'O'
            test = minmax(board, True)
            if test < best_score:
                best_score = test
                best_move = i
            board[i] = ' '
    return best_move

def read_move(board, x_turn):
    invalid = False
    while True:
        print_board()
        if invalid: print("Invalid move, try again.")
        if x_turn: move = input("\'X\' Turn. Enter your move: ")
        else: move = input("\'O\' Turn. Enter your move: ")
        match move.lower():
            case 'a1': move = 6
            case 'a2': move = 3
            case 'a3': move = 0
            case 'b1': move = 7
            case 'b2': move = 4
            case 'b3': move = 1
            case 'c1': move = 8
            case 'c2': move = 5
            case 'c3': move = 2
            case _:
                invalid = True
                continue
        if board[move] == ' ':
            if x_turn: board[move] = 'X'
            else: board[move] = 'O'
            return
        else: invalid = True
        
def game_loop():
    winner = None
    player_moves_first = start_game()
    if player_moves_first:
        bot_symbol = 'O'
    else:
        bot_symbol = 'X'
    for i in range(SIZE):
        if player_moves_first:
            if i % 2 == 0: player_turn = True
            else: player_turn = False
        else: 
            if i % 2 == 0: player_turn = False
            else: player_turn = True
        if not player_turn:
            move = bot_move(board, bot_symbol)
            board[move] = bot_symbol
        else: read_move(board, player_moves_first)
        if i > 3:
            validator = check_winner(board)
            match validator:
                case None:
                    continue
                case 'X':
                    winner = 'X'
                case 'O':
                    winner = 'O'
            break
    winner = check_winner(board)
    print_board()
    if winner == 'X': print("\'X\' won, game over.")
    elif winner == 'O': print("\'O\' won, game over.")
    else: print("Draw, game over.")

def start_game():
    invalid = False
    while True:
        clear_cli()
        if invalid: print("Invalid choice, try again.")
        player = input("Choose your symbol, \'X\' or \'O\' (\'X\' plays first): ")
        if player.upper() == 'X': return True
        elif player.upper() == 'O': return False
        else: invalid = True

game_loop()