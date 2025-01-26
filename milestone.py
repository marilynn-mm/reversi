# Nicolas Riley and Marilyn Ma
# Text-Based Game Project
       
import time 
import random 

class Board:
    """A data type representing a Reversi board
    with an arbitrary number of rows and columns.
    A board has three data members
    A variable data storing the two-dimensional array (list of lists), which is the game board
    A variable height storing the number of rows on the game board
    A variable width storing the number of columns on the game board
    """


    def __init__(self, height, width):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]
        
    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                        
        for row in range(0, self.height):
            s += "  " + 33 * '-' + "\n" 
            s += str(int(row)) + " " + '|' + " "
            for col in range(0, self.width):
                s += self.data[row][col] + ' | '            
            s += '\n' 
        
        s += "  " + 33 * '-' + "\n"  
        
        s += " "
        for col in range (0,self.width):
            s += "   " + str(col%10)  

        return s   
    
    def setUp(self):
        """
        start the game with 4 in the middle 
        """
        for row in range(self.height):
            for col in range(self.width):
                self.data[row][col] = ' '

        self.data[3][3] = 'X'
        self.data[4][4] = 'X'
        self.data[3][4] = 'O'
        self.data[4][3] = 'O'

    def addMove(self, row, col, ox):
        """
        add a move to the board
        takes three arguments:
        row, represents the index of the row to which the checker will be added
        col, represents the index of the column to which the checker will be added
        ox, will be a 1-character string representing the checker to add to the board
        """
        if self.data[row][col] == ' ':
            self.data[row][col] = ox
        else:
            print("invalid move")

    def removeMove(self, row, col):
        """
        remove move
        """
        self.data[row][col] = " "


    def FlipMove(self, row, col):
        """
        This method will flip an "X" to an "O" and vice versa to allow for the flipping
        element of a Reversi turn

        row, represents the index of the row to which the checker will be flipped
        col, represents the index of the column to which the checker will be flipped
        ox, will be a 1-character string representing the checker to add to the flipped    
        """
        
        if self.data[row][col] == "X":
            self.data[row][col] = "O"
        elif self.data[row][col] == "O":
            self.data[row][col] = "X"

    def fullBoard(self):
        """
        set all board spaces to X
        """
        for col in range(0, self.width):
            for row in range(0, self.height):
                self.data[row][col] = random.choice(['X','O'])


# checking allowsMove |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

    def checkE(self, s_row, s_col, ox):
        """
        Checks that a move is legal according to the East direction.
        The move must be next to the opposite checker and must have at 
        least of its own checker somewhere down the line 
        """
        if ox == "X": 
            ox2 = "O"
        if ox == "O": 
            ox2 = "X"

        if s_col + 1 >= self.width:
            return False 

        if self.data[s_row][s_col+1] == ox or self.data[s_row][s_col+1] == " ":
            return False 
        
        i = 1
        while s_col + i < self.width - 1 and self.data[s_row][s_col+i] == ox2:
            i += 1
        
        if self.data[s_row][s_col+i] == " ":
            return False

        if self.data[s_row][s_col+i] == ox:
            return True 

    def checkW(self, s_row, s_col, ox):
        """
        Checks that a move is legal according to the West direction.
        The move must be next to the opposite checker and must have at 
        least of its own checker somewhere down the line 
        """
        if ox == "X": 
            ox2 = "O"
        if ox == "O": 
            ox2 = "X"

        if s_col - 1 <= 0:
            return False 
        
        if self.data[s_row][s_col-1] == ox or self.data[s_row][s_col-1] == " ":
            return False 
    
        i = 1
        while s_col - i > 0 and self.data[s_row][s_col-i] == ox2:
            i += 1
        
        if self.data[s_row][s_col-i] == " ":
            return False

        if self.data[s_row][s_col-i] == ox:
            return True 

    def checkN(self, s_row, s_col, ox):
        """
        Checks that a move is legal according to the North direction.
        The move must be next to the opposite checker and must have at 
        least of its own checker somewhere down the line 
        """
        if ox == "X": 
            ox2 = "O"
        if ox == "O": 
            ox2 = "X"

        if s_row + 1 <= 0:
            return False 

        if self.data[s_row-1][s_col] == ox or self.data[s_row-1][s_col] == " ":
            return False 
    
        i = 1
        while s_row - i > 0 and self.data[s_row-i][s_col] == ox2:
            i += 1
        
        if self.data[s_row-i][s_col] == " ":
            return False

        if self.data[s_row-i][s_col] == ox:
            return True 


    def checkS(self, s_row, s_col, ox):
        """
        Checks that a move is legal according to the South direction.
        The move must be next to the opposite checker and must have at 
        least of its own checker somewhere down the line 
        """
        if ox == "X": 
            ox2 = "O"
        if ox == "O": 
            ox2 = "X"

        if s_row + 1 >= self.height:
            return False 
        
        if self.data[s_row+1][s_col] == ox or self.data[s_row+1][s_col] == " ":
            return False 
    
        i = 1
        while s_row + i < self.height - 1 and self.data[s_row+i][s_col] == ox2:
            i += 1
        
        if self.data[s_row+i][s_col] == " ":
            return False

        if self.data[s_row+i][s_col] == ox:
            return True 


    def checkSE(self, s_row, s_col, ox):
        """
        Checks that a move is legal according to the Southeast direction.
        The move must be next to the opposite checker and must have at 
        least of its own checker somewhere down the line 
        """
        if ox == "X": 
            ox2 = "O"
        if ox == "O": 
            ox2 = "X"

        if s_row + 1 >= self.height or s_col + 1 >= self.width:
            return False 
        
        if self.data[s_row+1][s_col+1] == ox or self.data[s_row+1][s_col+1] == " ":
            return False 
    
        i = 1
        while s_row + i < self.height - 1 and s_col + i < self.width - 1 and self.data[s_row+i][s_col+i] == ox2:
            i += 1
        
        if self.data[s_row+i][s_col+i] == " ":
            return False

        if self.data[s_row+i][s_col+i] == ox:
            return True 

    def checkSW(self, s_row, s_col, ox):
        """
        Checks that a move is legal according to the Southwest direction.
        The move must be next to the opposite checker and must have at 
        least of its own checker somewhere down the line 
        """
        if ox == "X": 
            ox2 = "O"
        if ox == "O": 
            ox2 = "X"

        if s_row + 1 >= self.height or s_col - 1 <= 0:
            return False 

        if self.data[s_row+1][s_col-1] == ox or self.data[s_row+1][s_col-1] == " ":
            return False 
    
        i = 1
        while s_row + i < self.height - 1 and s_col - i > 0 and self.data[s_row+i][s_col-i] == ox2:
            i += 1
        
        if self.data[s_row+i][s_col-i] == " ":
            return False

        if self.data[s_row+i][s_col-i] == ox:
            return True 

    def checkNW(self, s_row, s_col, ox):
        """
        Checks that a move is legal according to the Northwest direction.
        The move must be next to the opposite checker and must have at 
        least of its own checker somewhere down the line 
        """
        if ox == "X": 
            ox2 = "O"
        if ox == "O": 
            ox2 = "X"

        if s_row + 1 <= 0 or s_col - 1 <= 0:
            return False 

        if self.data[s_row-1][s_col-1] == ox or self.data[s_row-1][s_col-1] == " ":
            return False 
    
        i = 1
        while s_row - i > 0 and s_col - i > 0 and self.data[s_row-i][s_col-i] == ox2:
            i += 1
        
        if self.data[s_row-i][s_col-i] == " ":
            return False

        if self.data[s_row-i][s_col-i] == ox:
            return True 

    def checkNE(self, s_row, s_col, ox):
        """
        Checks that a move is legal according to the Northeast direction.
        The move must be next to the opposite checker and must have at 
        least of its own checker somewhere down the line 
        """
        if ox == "X": 
            ox2 = "O"
        if ox == "O": 
            ox2 = "X"

        if s_row - 1 <= 0 or s_col + 1 >= self.width:
            return False 
        
        if self.data[s_row-1][s_col+1] == ox or self.data[s_row-1][s_col+1] == " ":
            return False 
    
        i = 1
        while s_row - i > 0 and s_col + i < self.width - 1 and self.data[s_row-i][s_col+i] == ox2:
            i += 1
        
        if self.data[s_row-i][s_col+i] == " ":
            return False

        if self.data[s_row-i][s_col+i] == ox:
            return True 
    
    def checkAll(self, s_row, s_col, ox):
        """
        To check for all directions that a 'sandwich' can be made i.e. in XOOOX, OOO is sandwwiched by two X's 
        """
        if self.checkN(s_row, s_col, ox):
            return True
        if self.checkE(s_row, s_col, ox):
            return True
        if self.checkW(s_row, s_col, ox):
            return True
        if self.checkS(s_row, s_col, ox):
            return True
        if self.checkNE(s_row, s_col, ox):
            return True
        if self.checkNW(s_row, s_col, ox):
            return True
        if self.checkSE(s_row, s_col, ox):
            return True
        if self.checkSW(s_row, s_col, ox):
            return True
        return False

    def allowsMove(self, r, c, ox):
        """This method should return True if the calling object (of type Board)
        does allow a move into row r and column c. It returns False if row r or
        column c are not legal row and column numbers respectively. It also returns
        False if the board is full.
        """
        if c < 0 or c > self.width - 1:
            return False
        elif r < 0 or r > self.height - 1:
            return False
        elif self.data[r][c] != ' ':
            return False
        elif self.checkAll(r, c, ox):
            return True
        else: 
            return False


# flip moves in different directions |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

    def flipE(self, s_row, s_col, ox):
        """
        if add a move is legal in E direction, flip all the related checkers on the East Side 
        """
        if ox == "X": 
            ox2 = "O"
        if ox == "O": 
            ox2 = "X"

        if self.checkE(s_row, s_col, ox):
            i = 1
            while self.data[s_row][s_col+i] == ox2:
                self.FlipMove(s_row, s_col+i)
                i += 1

    def flipW(self, s_row, s_col, ox):
        """
        if add a move is legal in W direction, flip all the related checkers on the West Side 
        """
        if ox == "X": 
            ox2 = "O"
        if ox == "O": 
            ox2 = "X"

        if self.checkW(s_row, s_col, ox):
            i = 1
            while self.data[s_row][s_col-i] == ox2:
                self.FlipMove(s_row, s_col-i)
                i += 1

    def flipN(self, s_row, s_col, ox):
        """
        if add a move is legal in N direction, flip all the related checkers on the N Side 
        """
        if ox == "X": 
            ox2 = "O"
        if ox == "O": 
            ox2 = "X"

        if self.checkN(s_row, s_col, ox):
            i = 1
            while self.data[s_row-i][s_col] == ox2:
                self.FlipMove(s_row-i, s_col)
                i += 1

    def flipS(self, s_row, s_col, ox):
        """
        if add a move is legal in S direction, flip all the related checkers on the South Side 
        """
        if ox == "X": 
            ox2 = "O"
        if ox == "O": 
            ox2 = "X"

        if self.checkS(s_row, s_col, ox):
            i = 1
            while self.data[s_row+i][s_col] == ox2:
                self.FlipMove(s_row+i, s_col)
                i += 1

    def flipNE(self, s_row, s_col, ox):
        """
        if add a move is legal in NE direction, flip all the related checkers on the NE Side 
        """
        if ox == "X": 
            ox2 = "O"
        if ox == "O": 
            ox2 = "X"

        if self.checkNE(s_row, s_col, ox):
            i = 1
            while self.data[s_row-i][s_col+i] == ox2:
                self.FlipMove(s_row-i, s_col+i)
                i += 1

    def flipNW(self, s_row, s_col, ox):
        """
        if add a move is legal in NW direction, flip all the related checkers on the north west Side 
        """
        if ox == "X": 
            ox2 = "O"
        if ox == "O": 
            ox2 = "X"

        if self.checkNW(s_row, s_col, ox):
            i = 1
            while self.data[s_row-i][s_col-i] == ox2:
                self.FlipMove(s_row-i, s_col-i)
                i += 1

    def flipSE(self, s_row, s_col, ox):
        """
        if add a move is legal in SE direction, flip all the related checkers on the South East Side 
        """
        if ox == "X": 
            ox2 = "O"
        if ox == "O": 
            ox2 = "X"

        if self.checkSE(s_row, s_col, ox):
            i = 1
            while self.data[s_row+i][s_col+i] == ox2:
                self.FlipMove(s_row+i, s_col+i)
                i += 1
    
    def flipSW(self, s_row, s_col, ox):
        """
        if add a move is legal in SW direction, flip all the related checkers on the South West Side 
        """
        if ox == "X": 
            ox2 = "O"
        if ox == "O": 
            ox2 = "X"

        if self.checkSW(s_row, s_col, ox):
            i = 1
            while self.data[s_row+i][s_col-i] == ox2:
                self.FlipMove(s_row+i, s_col-i)
                i += 1

    def flipAll(self, s_row, s_col, ox):
        """
        flip all legal moves 
        """
        self.flipE(s_row, s_col, ox)
        self.flipS(s_row, s_col, ox)
        self.flipW(s_row, s_col, ox)
        self.flipN(s_row, s_col, ox)
        self.flipSE(s_row, s_col, ox)
        self.flipSW(s_row, s_col, ox)
        self.flipNE(s_row, s_col, ox)
        self.flipNW(s_row, s_col, ox)
        
# counting / checking winning condition |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

    def isFull(self):
        """This method should return True if the calling object (of type Board)
        is completely full of checkers. It should return False otherwise.
        """        

        for col in range(0, self.width):
            for row in range(0, self.height):
                if self.data[row][col] == ' ':
                    return False

        return True

    def countX(self):
        """
        Count the number of X on the board
        Return Integer
        """
        # suppose a reversi board has 64 open spots, so if all 64 are taken, the game is over
        
        countX = 0 

        for col in range(0, self.width):
            for row in range(0, self.height):
                if self.data[row][col] == 'X':
                    countX += 1
        return countX

    def countO(self):
        """
        Count the number of O on the board
        Return Integer
        """
        # suppose a reversi board has 64 open spots, so if all 64 are taken, the game is over
        
        countO = 0 

        for col in range(0, self.width):
            for row in range(0, self.height):
                if self.data[row][col] == 'O':
                    countO += 1
        return countO
    
    def winFor(self):
        """
        Check win when board is full 
        """

        # if self.isFull == "False":
        #     print ("Board is not full! Keep Playing")
        fullboard = self.width * self.height
        print("X has {}/{} pieces".format(self.countX(), fullboard))
        print("O has {}/{} pieces".format(self.countO(), fullboard))

        if self.isFull(): 
            if self.countX() > self.countO():
                print("X wins by", int(self.countX())-int(self.countO()), "pieces")
            if self.countO() > self.countX():
                print("O wins by", int(self.countO())-int(self.countX()), "pieces")
            if self.countX() == self.countO():
                print ("It's a Draw")

            print ()
            print("Do you want to play again?")
            print("If yes, please type in...")
            print("1. Enter 'b.hostGame' for player vs player \n 2. Enter 'b.hostRAIGame' for player vs Random AI \n 3. Enter 'b.host2AIGame' for AI vs AI \n 4. Enter 'b.hostSmartAIGame' for player vs Smart AI " )


# Smart AI |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

    def copy(self):
        """
        create a deep copy of itself
        """
        copy = Board(self.height, self.width)
        copy.data = [row[:] for row in self.data]
        return copy
    
    def scoreOfMoveX(self, row, col):
        """
        Calculate the score change as a result of a "X" move.
        Returns score_change: The change in score after the move.
        """

        temp_board = self.copy()
        temp_board.reversiMove(row,col,"X")

        # Calculate the score before and after the move
        s1 = self.countX()
        s2 = temp_board.countX()

        score_change = abs(s2 - s1)

        return score_change


    def scoreOfMoveO(self, row, col):
        """
        Calculate the score change as a result of a "X" move.
        Returns score_change: The change in score after the move.
        """

        temp_board = self.copy()
        temp_board.reversiMove(row,col,"O")

        # Calculate the score before and after the move
        s1 = self.countO()
        s2 = temp_board.countO()

        score_change = abs(s2 - s1)

        return score_change

    def listOfMoves(self, ox):
        """create a list of avaiable moves
        for the AI to pick from
        assign score of move
        """

        listOfMoves = []

        for col in range(0, self.width):
            for row in range(0, self.height):
                if self.allowsMove(row, col, ox) == True:
                    #listOfMoves += [{row, col}]
                    listOfMoves.append((row, col))
        
        return listOfMoves


    def listOfMaxMove(self, ox):
        """from list of move
        find move/moves with highest score
        """

        listOfMoves = []

        for col in range(0, self.width):
            for row in range(0, self.height):
                if self.allowsMove(row, col, ox) == True:
                    #listOfMoves += [{row, col}]
                    score = self.scoreOfMoveX(row, col) if ox == "X" else self.scoreOfMoveO(row, col)
                    listOfMoves.append((score, row, col))

        if not listOfMoves:
            return [] 
        
        max_score = max(move[0] for move in listOfMoves)
        listOfMaxMove = [(score, row, col) for score, row, col in listOfMoves if score == max_score]
        return listOfMaxMove

    def listOfEmptyCells(self):
        """from list of move
        find list of empty move/moves
        """

        listOfEmptyMoves = []

        for col in range(0, self.width):
            for row in range(0, self.height):
                if self.data[row][col] == " ":
                    listOfEmptyMoves.append((row, col))

        return listOfEmptyMoves
    
# Reversi Move |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


    def reversiMove(self, row, col, ox):
        """
        adding move in accordance to reversi rules 
        flip associated moves
        """
        if self.allowsMove(row, col, ox) == False:
            print ("Invalid Move, try again")
            
        elif self.allowsMove(row, col, ox):
            self.addMove(row, col, ox)
            self.flipAll(row, col, ox)

    def randomAIMove(self, ox):
        """
        Ai places randomly on the board 
        """
        
        validMoves = []
        for row in range(self.height):
            for col in range(self.width):
                if self.allowsMove(row, col, ox):
                    validMoves.append((row, col))
                
        if not validMoves:
            print("No valid moves available.")
            return  # Exit the function if there are no valid moves

        random_pair = random.choice(validMoves)
        row, col = random_pair 
        self.reversiMove(row, col, ox)

    def smartAIMove(self, ox):
        """
        Ai places the move with max flips
        randomized if multiple spots have the same
        """
        x = random.choice (self.listOfMaxMove(ox))
        self.reversiMove(x[1], x[2], ox)

# host game |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

        
    def hostGame(self):
        """
        host a game of reversi between two human players
        alternate turns between 'X' (who will always go first) and 'O' (who will always go second)
        ask the users (with the input function) to select a column number for each move
        """

        b.setUp()
        print(b)  
        
        ox = 'X'  

        while True:
            userrow = -1
            usercolumn = -1
            while self.allowsMove(userrow, usercolumn, ox) == False:
                userstring1 = input(f"{ox}'s choice of row: ")
                userstring2 = input(f"{ox}'s choice of column: ")
                try:
                    userrow = int(userstring1)
                    usercolumn = int(userstring2)
                    if self.allowsMove(userrow, usercolumn, ox):
                        break
                    else:
                        print("Move not allowed. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter integers for row and column.")
                    continue
                        
            self.reversiMove(userrow, usercolumn, ox)
            print(self) 
                
            if ox == "X":
                ox = "O"
            elif ox == "O":
                ox = "X"

            if self.isFull():
                break 
        
        self.winFor()
    
    #host game AI function 
    
    def hostRAIGame(self):
        """
        host a game of reversi between a human and an AI that plays randomly
        alternate turns between 'X' (who will always go first) and 'O' (who will always go second) 
        ask the user (with the input function) to select a column number for each move
        """
        b.setUp()
        print(b)  
        
        ox = 'X'  

        while True:
            userrow = -1
            usercolumn = -1
            while self.allowsMove(userrow, usercolumn, ox) == False:
                userstring1 = input(f"{ox}'s choice of row: ")
                userstring2 = input(f"{ox}'s choice of column: ")
                try:
                    userrow = int(userstring1)
                    usercolumn = int(userstring2)
                    if self.allowsMove(userrow, usercolumn, ox):
                        break
                    else:
                        print("Move not allowed. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter integers for row and column.")
                    continue
            
            self.reversiMove(userrow, usercolumn, ox)
            print(self) 
                
            print("AI's move...")
            time.sleep(2)
            self.randomAIMove("O")
            print(self)

            if self.isFull():
                break 
        
        self.winFor()

    def host2AIGame(self):
        """
        host a game of reversi between two AI that both play randomly
        alternate turns between 'X' (who will always go first) and 'O' (who will always go second)
        ask the user (with the input function) to select a column number for each move
        """
        b.setUp()
        print(self)  
        
        ox = 'X'  
        ox2 = 'O'
        while True:

            print("AI 1's move...")
            # time.sleep(1)
            if self.listOfMoves(ox) != []:
                self.smartAIMove(ox)
            print(self)


            print("AI 2's move...")
            # time.sleep(1)
            if self.listOfMoves(ox2) != []:
                self.smartAIMove(ox2)
            print(self)
            
            if not self.isFull():
                if self.listOfMoves(ox) == [] and self.listOfMoves(ox2) == []:
                    self.addMove(random.choice(self.listOfEmptyCells), ox2) 
                    #remove the bracket 
                    

            if self.isFull():
                break 
        
        self.winFor()

    def hostSmartAIGame(self):
        """
        host a game of reversi between a human and a smart AI.
        The game alternates turns between 'X' (who will always go first) and 'O' (who will always go second) 
        ask the user (with the input function) to select a column number for each move
        """

        b.setUp()
        print(b)  
        
        ox = 'X'  

        while True:
            userrow = -1
            usercolumn = -1
            while self.allowsMove(userrow, usercolumn, ox) == False:
                userstring1 = input(f"{ox}'s choice of row: ")
                userstring2 = input(f"{ox}'s choice of column: ")
                try:
                    userrow = int(userstring1)
                    usercolumn = int(userstring2)
                    if self.allowsMove(userrow, usercolumn, ox):
                        break
                    else:
                        print("Move not allowed. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter integers for row and column.")
                    continue
            
            self.reversiMove(userrow, usercolumn, ox)
            print(self) 
                
            print("AI's move...")
            # time.sleep(2)
            self.smartAIMove("O")
            print(self)

            if self.isFull():
                break 
        
        self.winFor()


# game instruction |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

b = Board(8,8)
b.setUp()

print("Welcome to Reversi. The following game modes are available: \n 1. Enter 'b.hostGame' for player vs player \n 2. Enter 'b.hostRAIGame' for player vs Random AI \n 3. Enter 'b.host2AIGame' for AI vs AI \n 4. Enter 'b.hostSmartAIGame' for player vs Smart AI ")
