import numpy as np

class tic_tac_toe():
    """
    A class to represent the Tic-Tac-Toe game.
    
    The class allows two players to play Tic-Tac-Toe, alternating between 'X' and 'O'. It handles 
    the initialization of the board, making moves, checking for a winner, and determining whether
    the game continues or ends.

    Attributes:
        board (str): A string representing the layout of the Tic-Tac-Toe board.
        play (dict): A dictionary tracking the current state of the game board (e.g., 'X', 'O', or empty).
        continue_game (bool): A flag to indicate whether the game should continue or end.
        winner (int): A variable to hold the winner (1 for player 1, 2 for player 2, 0 for no winner).
    """
    
    def __init__(self):
        """Initialize the game board and game state."""
        self.board='''
        {s1:^3} | {s2:^3} | {s3:^3}
        ----+-----+-----
        {s4:^3} | {s5:^3} | {s6:^3}
        ----+-----+-----      
        {s7:^3} | {s8:^3} | {s9:^3}      
                            
        '''
        self.play= {}
        
        self.continue_game=True
        self.winner=0
        
    def initialize_board(self):
        """Initialize the game board with empty spaces for each square (s1 to s9)."""
        for n in range(9):
            self.play["s{}".format(n+1)] = ""
    
    def show_board(self):
        """Display the current game board using the dictionary `self.play` to populate the board template."""
        print(self.board.format(**self.play))

    def get_move(self, n: int, xo: str):
        """Ask the current player to make a move. Ensures the selected square is empty.

        Args:
            n (int): The current player's number (1 or 2).
            xo (str): The player's mark ('X' or 'O').

        This method will continue to ask for input until a valid move is made.
        """
        valid_move = False
        while not valid_move:
            idx = input("player {}, enter your move (1-9)".format(n))
            if self.play["s{}".format(idx)] == "":
                key="s{}".format(idx)
                self.play[key]=xo
                valid_move = True
            else:
                print("invalid: {}".format(self.play["s{}".format(idx)]))
    
    def check_game(self):
        
        """Check the current game state for a winner or tie.

        This method checks the rows, columns, and diagonals for a winning combination. 
        If all squares are filled and no winner, it results in a tie.
        """
        signs=np.array([sign for _,sign in self.play.items()])
        
        #create the matrix with the signs
        signs_matrix=signs.reshape(3,3) #it's possible to interpretate that as the array of the rows
        columns_array=signs_matrix.T
        diagonals=[np.diag(signs_matrix),np.diag(np.fliplr(signs_matrix))]#Retrive the diagonals
        
        def check_matrix(matrix):
            """Check each row, column, or diagonal for a winner.

            Args:
                matrix (numpy.array): The matrix representing rows, columns, or diagonals.

            Returns:
                bool: False if a winner is found, True otherwise.
            """
            for array in matrix:
                if all(element=="X" for element in array):
                    self.winner=1
                    return False
                elif all(element=="O" for element in array):
                    self.winner=2
                    return False
            return True #If the matrix has no all the signs equal the game must contiue
        self.continue_game=check_matrix(signs_matrix) and check_matrix(columns_array) and check_matrix(diagonals) and np.any(signs_matrix == "")
        
    def play_game(self):
        """Play a game of Tic-Tac-Toe, alternating turns between two players.

        This method runs the game loop, asking players to make moves, updating the board,
        and checking for a winner after each turn.
        """
        player=1
        self.play ={}
        
        self.initialize_board()
        self.show_board()
        
        while self.continue_game:
            if player==1:
                player_mark="X"
            elif player==2:
                player_mark="O"
            else:
                raise "Invalid Player"
            self.get_move(player,player_mark)
    
            self.show_board()
            
            self.check_game()
            #change the player
            if player==1:
                player=2
            else:
                player=1
            
            if self.winner==0:
                winner_string="There is no winner, is a tie!"
            else:
                winner_string=f"The winner is player {self.winner}"
        print(f"Game endend! \n {winner_string}")
        
        restart=input("Do you want to play again?(y/n)")
        
        if restart=="y":
            print("Have fun!")
            #Reset the variable for a new game
            self.continue_game=True
            self.winner=0
            self.play_game()
        else:
            print("See you soon!")


#=======================Pascal's Triangel========================
class Pascal_Triangle():
    """A Pascal Triangle calass
    """
    def __init__(self,n_layer=6):
        self.n_layer=n_layer
        if self.n_layer>1:
            self.construct_triangle()
        else:
            self.triangle=np.array([[1]])
    
    def print_triangle(self):
        """Print the Pascal's triangle in a readable format."""
        space_width = 2
        
        for row in self.triangle.astype(int):
            print(" ".join(f"{x:>{space_width}}" if x != 0 else " " * space_width for x in row))
            
    def construct_triangle(self):
        """Construct Pascal's triangle by generating each layer based on the previous one."""
        # Generate at list a mono dimensional triangle
        first_layer=np.zeros(2*self.n_layer-1)
        first_layer[self.n_layer-1]=1
        self.triangle=[first_layer]
        while len(self.triangle)< self.n_layer:
            last_layer=self.triangle[-1]
            left_layer=np.append(last_layer[1:],0)
            right_layer=np.append(0,last_layer[:-1])
            new_layer=left_layer+right_layer
            self.triangle.append(new_layer)
        self.triangle=np.array(self.triangle)

#=============developing section===========================0
if __name__ == "__main__":
    right_choice=False
    while not right_choice:
        choice=input("Do you want to play tick tack toe (1) or two see the Pascal's triangle(2)?")
        choice=int(choice)#Convert the input string to a integer
        if choice==1 or choice==2:
            right_choice=True
        else:
            print(f"Invalid choice: {choice}")
    
    if choice==1:
        print("Have fun with tic tack toe")        
        Game=tic_tac_toe()

        Game.play_game()
    else:
        n_layer=0
        while type(n_layer) is not int or n_layer==0:
            n_layer=input("How many layer do you want for the Pascal's triangle?")
            n_layer=int(n_layer)#Convert the input string to a integer
            if type(n_layer) is not int or n_layer==0:
                print("Invalid input, the input must be a integer > 0.")
        P_triangle=Pascal_Triangle(n_layer)
        P_triangle.print_triangle()
