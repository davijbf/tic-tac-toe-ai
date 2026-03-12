import os

SIZE = 9

def clear_cli():
    os.system('cls' if os.name == 'nt' else 'clear')

board = [' ' for _ in range(SIZE)]


def print_board():
    print(
    f"\n3  {board[0]} | {board[1]} | {board[2]}\n" \
    "  -----------\n" \
    f"2  {board[3]} | {board[4]} | {board[5]}\n" \
    "  -----------\n" \
    f"1  {board[6]} | {board[7]} | {board[8]}\n" \
    "   a   b   c\n")

def check_winner(table):
    x_won = False
    o_won = False
    # Checking rows
    for i in range(0, 9, 3):
        if table[i] != ' ' and table[i] == table[i+1] == table[i+2]:
            if table[i] == 'X':
                x_won = True
            else:
                o_won = True
    # Checking colunms
    for i in range(3):
        if table[i] != ' ' and table[i] == table[i+3] == table[i+6]:
            if table[i] == 'X':
                x_won = True
            else:
                o_won = True
    
    # Checking diagonals
    if table[0] != ' ' and table[0] == table[4] == table[8]:
        if table[0] == 'X':
                x_won = True
        else:
            o_won = True
    
    if table[2] != ' ' and table[2] == table[4] == table[6]:
        if table[2] == 'X':
                x_won = True
        else:
            o_won = True

    if x_won:   return 'X'
    elif o_won: return 'O'
    else:
        if avalible_moves(table): return None
        else: return 'draw'
    
def avalible_moves(table):
    moves = []
    for i in range(SIZE):
        if table[i] == ' ':
            moves.append(i)
    return moves

def check_avalible(table):
    for i in range(SIZE):
        if table[i] == ' ':
            return True
    return False

def minmax(table, is_max):
    result = check_winner(table)
    if result:
            result = check_winner(table)
            if result:
                if result == 'X': return 1
                elif result == 'O': return -1
                else : return 0
    else:
        avalible = avalible_moves(table)
        if is_max:
            best_score = -2
            for i in avalible:
                table[i] = 'X'
                best_score = max(minmax(table, False), best_score)
                table[i] = ' '     
        else:
            best_score = 2
            for i in avalible:
                table[i] = 'O'
                best_score = min(minmax(table, True), best_score)
                table[i] = ' '
        return best_score
    
def bot_move(table, turn):
    avalible = avalible_moves(table)
    if turn == 'X':
        best_score = -2
        best_move = -1
        for i in avalible:
            table[i] = 'X'
            test = minmax(table, False)
            if test > best_score:
                best_score = test
                best_move = i
            table[i] = ' '
    else:
        best_score = 2
        best_move = 1
        for i in avalible:
            table[i] = 'O'
            test = minmax(table, True)
            if test < best_score:
                best_score = test
                best_move = i
                table[i] = ' '

    return best_move


        


def read_move(x_turn):
    invalid = False
    while True:
        clear_cli()
        print_board()
        if invalid:
            print("Invalid move, try again.")
        if x_turn:
            move = input("\'X\' Turn. Enter your move: ")
        else:
            move = input("\'O\' Turn. Enter your move: ")
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
            if x_turn:
                board[move] = 'X'
            else:
                board[move] = 'O'
            return
        else:
            invalid = True
        
def game_loop():
    winner = None
    for i in range(SIZE):
        if i % 2 == 0:
            x_turn = True
        else:
            x_turn = False
        if x_turn:
            move = bot_move(board, 'X')
            board[move] = 'X'
        else:
            read_move(x_turn)
        if i > 3:
            validator = check_winner(board)
            match validator:
                case None:
                    continue
                case 'X':
                    winner = 'X'
                case 'O':
                    winner = 'O'
                case _:
                    winner = 'draw'
            break
                
    clear_cli()
    print_board()
    if winner == 'X':
        print("\'X\' won, game over.")
    elif winner == 'O':
        print("\'O\' won, game over.")
    else:
        print("Draw, game over.")