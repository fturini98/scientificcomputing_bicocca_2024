print('Modulo prima lezione')
import numpy as np

class tic_tac_toe():
    def __init__(self):
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
        for n in range(9):
            self.play["s{}".format(n+1)] = ""
    
    def show_board(self):
        """ display the playing board.  We take a dictionary with the current state of the board
        We rely on the board string to be a global variable"""
        print(self.board.format(**self.play))
                
    def get_move(self,n, xo):
        """ ask the current player, n, to make a move -- make sure the square was not 
            already played.  xo is a string of the character (x or o) we will place in
            the desired square """
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
        signs=np.array([sign for _,sign in self.play.items()])
        
        #create the matrix with the signs
        signs_matrix=signs.reshape(3,3) #it's possible to interpretate that as the array of the rows
        columns_array=signs_matrix.T
        diagonals=[np.diag(signs_matrix),np.diag(np.fliplr(signs_matrix))]#Retrive the diagonals
        def check_matrix(matrix):
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
        """ play a game of tic-tac-toe """

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
        
        restart=input("Do you want play again?(y/n)")
        
        if restart=="y":
            print("Have fun!")
            #Reset the variable for a new game
            self.continue_game=True
            self.winner=0
            self.play_game()
        else:
            print("See you soon!")


#=======================Pascal's triangel========================
class Pascal_triangle():
    def __init__(self,n_layer=6):
        self.n_layer=n_layer
        if self.n_layer>1:
            self.construct_triangle()
        else:
            self.triangle=np.array([[1]])
    
    def print_triangle(self):
        space_width = 2
        
        for row in self.triangle.astype(int):
            print(" ".join(f"{x:>{space_width}}" if x != 0 else " " * space_width for x in row))
            
    def construct_triangle(self):
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
        P_triangle=Pascal_triangle(n_layer)
        P_triangle.print_triangle()