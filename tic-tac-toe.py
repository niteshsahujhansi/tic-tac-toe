''' tic-tac-toe game in python '''

import random

# tic tac toe game methods inside the class TicTacToe 

class TicTacToe:
    
    def create_board(self) :

        ''' create 2D list/array of 3 rows and 3 colums and initialize all items with hyphen '''

        # using conventional method
        # self.board = []
        # # create board 
        # for i in range(3):
        #     col = []
        #     for j in range(3):
        #         col.append('-')
        #     self.board.append(col)

        # using list comprehension 
        self.board = [['-' for i in range(3)] for j in range(3)] 

    def show_board(self) :

        ''' this method print initialized board and used for further updated representation during match '''

        for row in self.board:
            for item in row:
                print(item, end=' ')
            print()
    
    def is_player_win(self, player) :

        ''' this is the most important method of this game  '''

        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:          # if any row is not filled by the same player
                    win = False                         
                    break
            if win:                    
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals 1
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True

        # checking diagonals 2
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win

        return False
        
    def is_board_full(self) :

        ''' return true if all places in the game are filled by the player's move,
            otherwise return false '''

        for row in self.board:
            for item in row:
                if item == '-':
                    return False 
        return True 

    def swap_player_turn(self,player) :

        ''' change the turn of the player'''

        # if player == 'X':
        #     player = 'O'
        # else:
        #     player = 'X'
        
        return 'O' if player == 'X' else 'X'
        


class main :

    ''' this is main Function '''

    # create object of TicTacToe class
    tictactoe = TicTacToe()
    
    # create board 
    tictactoe.create_board() 

    # show board
    tictactoe.show_board()

    # first turn is randomly chosen
    player = random.choice('X''O')
 
    while True:

        ''' infinite loop until one win the match or board is completely filled '''

        # shows which player has the turn
        
        print()
        print(f'player {player} turn')

        # taking input of row and column (3 ways are shown)

        # row = int(input('Enter row: '))
        # col = int(input('Enter Col: '))

        # using split map list function
        row, col = list(map(int, input('Enter (row, col) position: ').split()))

        # using list comprehension 
        # row, col = [int(x) for x in input("Enter two values: ").split()]

        # fix the move played by the player 
        tictactoe.board[row-1][col-1] = player 

        # shows updated board after the player's move
        tictactoe.show_board()

        # check for winning conditions if any condition met (true) execution comes inside this function
        # then print winning statement and terminate the main while loop 
        if tictactoe.is_player_win(player) :
            print()
            print(player, 'win the match.')
            break            
        
        # if no one win, then execution check for this function
        # if board is filled completely than print draw statment
        if tictactoe.is_board_full():
            print()
            print('Match Draw!')
            break 
        
        # if execution is not terminated by the above two functions
        # then the turn of the playerd is swaped (changed)
        player = tictactoe.swap_player_turn(player)
   

main() # calling main class, exicution starts from here