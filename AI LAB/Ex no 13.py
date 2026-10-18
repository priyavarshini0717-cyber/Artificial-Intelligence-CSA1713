def minimax(board, is_max):
    if 'X' in board and check(board, 'X'):
        return 1
    if 'O' in board and check(board, 'O'):
        return -1
    if ' ' not in board:
        return 0

    if is_max:
        best = -100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = max(best, minimax(board, False))
                board[i] = ' '
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = min(best, minimax(board, True))
                board[i] = ' '
        return best

def check(board, p):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    return any(board[a] == board[b] == board[c] == p
               for a,b,c in wins)

board = [' '] * 9

for turn in range(9):
    if turn % 2 == 0:
        pos = int(input("Enter position (1-9): ")) - 1
        if pos < 0 or pos > 8 or board[pos] != ' ':
            print("Invalid position!")
            continue
        board[pos] = 'O'
    else:
        best = -100
        move = -1
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, False)
                board[i] = ' '
                if score > best:
                    best = score
                    move = i
        board[move] = 'X'

    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

    if check(board, 'X'):
        print("Computer wins!")
        break
    if check(board, 'O'):
        print("Player wins!")
        break
else:
    print("Match Draw!")
