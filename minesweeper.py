import random

class Admin_Board:
    def __init__(self, rows, columns, bombs, row, column):
        self.rows = rows
        self.columns = columns
        self.bombs = bombs
        self.bomb_list = []

        self.row = row
        self.column = columns
        
        self.board = [[0 for row in range(self.rows)] for column in range(self.columns)]
        
        for i in range(self.bombs):
            x = random.randint(0,self.rows - 1)
            y = random.randint(0,self.columns - 1)
            if (x != self.row) and (y != self.column) and (self.board[x][y] != str("X")):
                self.board[x][y] = str("X")
            else:
                while (x == self.row) and (y == self.column) and (self.board[x][y] == str("X")):
                    x = random.randint(0,self.rows - 1)
                    y = random.randint(0,self.columns - 1)
                self.board[x][y] = str("X")
            self.bomb_list.append([x,y])

            #bomb not in last row (adds 1 to row above, same column)
            if (0 <= x < self.rows - 1) and (0 <= y <= self.columns - 1):
                if self.board[x+1][y] != "X":
                    self.board[x+1][y] += 1

            #bomb not in first row (adds 1 to row below, same column)
            if (0 < x <= self.rows -1) and (0 <= y <= self.columns - 1):
                if self.board[x-1][y] != "X":
                    self.board[x-1][y] += 1
            
            #bomb not in last column (adds 1 to same row, column to right)
            if (0 <= x <= self.rows - 1) and (0 <= y < self.columns - 1):
                if self.board[x][y+1] != "X":
                    self.board[x][y+1] += 1

            #bomb not in first column (adds 1 to same row, column to left)
            if (0 <= x <= self.rows -1) and (0 < y <= self.columns - 1):
                if self.board[x][y-1] != "X":
                    self.board[x][y-1] += 1

            #bomb not in last row or last column (adds 1 to row above, right diagonal)
            if (0 <= x < self.rows - 1) and (0 <= y < self.columns - 1):
                if self.board[x+1][y+1] != "X":
                    self.board[x+1][y+1] += 1

            #bomb not in last row or first column (adds 1 to row above, left diagonal)
            if (0 <= x < self.rows - 1) and (0 < y <= self.columns - 1):
                if self.board[x+1][y-1] != "X":
                    self.board[x+1][y-1] += 1

            #bomb not in first row or last column (adds 1 to row below, right diagonal)
            if (0 < x <= self.rows - 1) and (0 <= y < self.columns - 1):
                if self.board[x-1][y+1] != "X":
                    self.board[x-1][y+1] += 1
            
            #bomb not in first row or first column (adds 1 to row below, left diagonal)
            if (0 < x <= self.rows - 1) and (0 < y <= self.columns - 1):
                if self.board[x-1][y-1] != "X":
                    self.board[x-1][y-1] += 1

     
        
        
class Player_Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        
        self.player_board = [["-" for row in range(self.rows)] for column in range(self.columns)]
        



class Single_Turn:
    def __init__(self, admin_board, player_board, x, y, n, m):
        self.admin_board = admin_board
        self.player_board = player_board

        self.check = True

        if self.admin_board[n][m] != "X":
            self.player_board[n][m] = self.admin_board[n][m]

            if self.admin_board[n][m] == 0:
                
                #opens cell in row below, left diagonal
                if (0 < n <= x-1) and (0 < m <= y-1) and self.admin_board[n-1][m-1] != "X":
                    self.player_board[n-1][m-1] = self.admin_board[n-1][m-1]

                #opens cell in row below, same column
                if (0 < n <= x-1) and (0 <= m <= y-1) and self.admin_board[n-1][m] != "X":
                    self.player_board[n-1][m] = self.admin_board[n-1][m]

                #opens cell in row below, right diagonal
                if (0 < n <= x-1) and (0 <= m < y-1) and self.admin_board[n-1][m+1] != "X":
                    self.player_board[n-1][m+1] = self.admin_board[n-1][m+1]

                #opens cell in column to left
                if (0 <= n <= x-1) and (0 < m <= y-1) and self.admin_board[n][m-1] != "X":
                    self.player_board[n][m-1] = self.admin_board[n][m-1]

                #opens cell in column to right
                if (0 <= n <= x-1) and (0 <= m < y-1) and self.admin_board[n][m+1] != "X":
                    self.player_board[n][m+1] = self.admin_board[n][m+1]

                #opens cell in row above, left diagonal
                if (0 <= n < x-1) and (0 < m <= y-1) and self.admin_board[n+1][m-1] != "X":
                    self.player_board[n+1][m-1] = self.admin_board[n+1][m-1]

                #opens cell in row above, same column
                if (0 <= n < x-1) and (0 <= m <= y-1) and self.admin_board[n+1][m] != "X":
                    self.player_board[n+1][m] = self.admin_board[n+1][m]

                #opens cell in row above, right diagonal
                if (0 <= n < x-1) and (0 <= m < y-1) and self.admin_board[n+1][m+1] != "X":
                    self.player_board[n+1][m+1] = self.admin_board[n+1][m+1]

 
        else:
            self.check = False

               
        
   

class Game_Won_Check:
    def __init__(self, bomb_list, player_board):
        self.bomb_list = bomb_list
        self.player_board = player_board
    
        self.game_won = False
        self.dash_counter = sum(z.count("-") for z in self.player_board)

        if self.dash_counter == len(self.bomb_list):
            self.game_won = True
        else:
            pass
        
           


class Minesweeper:
    def __init__(self):
        
        play = "yes"
    
        print("")
        print("==============================")
        print("*** Welcome to Minesweeper ***")
        print("==============================")
        

        while play == "yes":

            r = 0
            c = 0
            b = 0

            difficulty = input("Choose difficulty (enter easy, medium, or hard): ")

            if difficulty == "easy":
                r = 5
                c = 5
                b = 2
            
            if difficulty == "medium":
                r = 7
                c = 7
                b = 5
            
            if difficulty == "hard":
                r = 9
                c = 9
                b = 8
                

            player = Player_Board(r, c)
            players_board = player.player_board
        

            print("")
            for row in players_board:
                print(" | ".join(str(cell) for cell in row))
                print("")
            
            
            continue_game = True
        
            row_n = int(input("Enter row (0 to {r}): ".format(r = (r-1))))
            column_m = int(input("Enter column (0 to {c}): ".format(c = (c -1))))

            admin = Admin_Board(r, c, b, row_n, column_m)
            admin_board = admin.board
            bomb_list = admin.bomb_list

            Single_Turn(admin_board, players_board, r, c, row_n, column_m)
            first_turn_check = Single_Turn(admin_board, players_board, r, c, row_n, column_m).check
            
            #checks to see if bomb is hit during first turn, if so new admin_board is made and [row_n, column_m] cell is opened on players_board
            if first_turn_check == False:

                while first_turn_check == False:
                    admin = Admin_Board(r, c, b, row_n, column_m)
                    admin_board = admin.board
                    bomb_list = admin.bomb_list

                players_board[row_n][column_m] = admin_board[row_n][column_m]


            while continue_game == True:
            
                print("")
                for row in players_board:
                    print(" | ".join(str(cell) for cell in row))
                    print("")
                


                row_n = int(input("Enter row (0 to {r}): ".format(r = (r-1))))
                column_m = int(input("Enter column (0 to {c}): ".format(c = (c-1))))
                
                
                Single_Turn(admin_board, players_board, r, c, row_n, column_m)

            
                if Single_Turn(admin_board, players_board, r, c, row_n, column_m).check == False:

                    print("")
                    print("=================")
                    print("*** GAME OVER ***")
                    print("=================")
                    print("")
                    
                    for row in admin_board:
                        print(" | ".join(str(cell) for cell in row))
                        print("")

                    continue_game = False


                if Game_Won_Check(bomb_list, players_board).game_won == True:

                    print("")
                    print("=================")
                    print("*** YOU WON!! ***")
                    print("=================")
                    print("")

                    for row in admin_board:
                        print(" | ".join(str(cell) for cell in row))
                        print("")

                    continue_game = False
                
            play = input("Would you like to play again? (enter yes or no): ")

        

            
Minesweeper()