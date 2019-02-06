import random

def tic_tac_toe():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    win_cases = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def draw():
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])
        print()

    def player():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nDo you even know the rules? Try again please.")
            player()
        else:
            board[n] = "X"

    def computer():
        n = random.randint(1,8)
        
        if board[n] == "X" or board[n] == "O":
            computer()
        else:
            board[n] = "O"

    def choose_number():
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nThat's not on the board. Try again")
                        continue
                except ValueError:
                   print("\nThat's not even a number.")
                   continue

    def check_board():
        count = 0
        for a in win_cases:
            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print("Player 1 Wins!\n")
                print("Congratulations!\n")
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print("Computer Wins!\n")
                print("You are such a loser\n")
                return True
        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("It's a tie\n")
                return True

    while not end:
        draw()
        end = check_board()
        if end == True:
            break
        print("Player 1 choose where to place a cross")
        player()
        print()
        draw()
        end = check_board()
        if end == True:
            break
        print("Computer is choosing where to place a nought")
        computer()
        print()

tic_tac_toe()
