theBoard = {'q': ' ' , 'w': ' ' , 'e': ' ' ,
            'a': ' ' , 's': ' ' , 'd': ' ' ,
            'z': ' ' , 'x': ' ' , 'c': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print('')
    print(board['q'] + ' | ' + board['w'] + ' | ' + board['e'])
    print('--+---+--')
    print(board['a'] + ' | ' + board['s'] + ' | ' + board['d'])
    print('--+---+--')
    print(board['z'] + ' | ' + board['x'] + ' | ' + board['c'])
    print('')
def game():
    turn = 'X'
    count = 0
    for i in range(10):
        printBoard(theBoard)
        print("It's your turn, " + turn + ". Move to which place?")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        if count >= 5:
            if theBoard['q'] == theBoard['w'] == theBoard['e'] != ' ': # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['a'] == theBoard['s'] == theBoard['d'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['z'] == theBoard['x'] == theBoard['c'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['z'] == theBoard['a'] == theBoard['q'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['x'] == theBoard['s'] == theBoard['w'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['c'] == theBoard['d'] == theBoard['e'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['q'] == theBoard['s'] == theBoard['c'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['z'] == theBoard['s'] == theBoard['e'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break

        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'

    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theBoard[key] = " "

        game()

if __name__ == "__main__":
    game()
