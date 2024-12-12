import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Game_life():
    """
    Class that implements Conway's Game of Life.
    The grid is initialized with a specified size and an initial condition.
    The default condition is a small glider.
    """
    
    def __init__(self,shape=(100,100),initial_condition="default"):
        """
        Initializes the grid with a specified shape and an initial condition.
        
        :param shape: Tuple specifying the grid shape (default is (100, 100)).
        :param initial_condition: The initial condition of the grid. "default" uses a predefined condition.
        """
        self.grid=np.zeros(shape=shape)
        self.shape=shape
        
        if initial_condition=="default":
            self.default_initial_condition()
    
    def show(self,ax):
        """
        Displays the grid on the given axes using a 'gray' colormap.
        
        :param ax: The Matplotlib Axes object where the grid will be displayed.
        """
        ax.imshow(self.grid,cmap="gray")

    
    def default_initial_condition(self):
        """
        Sets the default initial condition as a glider pattern in motion.
        """
        y=20
        x=20
        self.grid[(0+y),(1+x)]=1
        self.grid[(1+y),(0+x):(2+x)]=1
        self.grid[(2+y),(1+x):(3+x)]=1
    
    def next_gen(self):
        """
        Computes the next generation in Conway's Game of Life using the game's rules and a matrix shift trick.
        
        :return: The new grid configuration after evolution.
        """
        d_n=self.shift_up(self.grid)
        u_n=self.shift_down(self.grid)
        r_n=self.shift_left(self.grid)
        l_n=self.shift_right(self.grid)
        
        dr_n=self.shift_left(u_n)
        dl_n=self.shift_right(u_n)
        ur_n=self.shift_left(d_n)
        ul_n=self.shift_right(d_n)
        
        neighbors=d_n+dl_n+dr_n+l_n+r_n+u_n+ul_n+ur_n
        candidate_survivors=np.logical_or(neighbors==2, neighbors==3).astype(int)
        survivors=np.logical_and(self.grid==1,candidate_survivors==1).astype(int)
        new=np.logical_and(self.grid==0, neighbors==3).astype(int)

        new_pop=new+survivors
        self.grid=new_pop
        return new_pop
        
    def shift_up(self,grid):
        """
        Shifts the grid upwards.
        
        :param grid: The current grid to shift.
        :return: The grid with values shifted upwards.
        """
        down_neighbors=np.append(grid[1:,:],grid[0,:]).reshape(self.shape)
        return down_neighbors
    
    def shift_down(self,grid):
        """
        Shifts the grid downwards.
        
        :param grid: The current grid to shift.
        :return: The grid with values shifted downwards.
        """
        up_neighbors=np.append(grid[-1,:],grid[:-1,:]).reshape(self.shape)
        return up_neighbors
    
    def shift_left(self,grid):
        """
        Shifts the grid to the left.
        
        :param grid: The current grid to shift.
        :return: The grid with values shifted to the left.
        """
        right_neighbors=np.append(grid.T[1:,:],grid.T[0,:]).reshape(self.shape).T
        return right_neighbors
    
    def shift_right(self,grid):
        """
        Shifts the grid to the right.
        
        :param grid: The current grid to shift.
        :return: The grid with values shifted to the right.
        """
        left_neigbors=np.append(grid.T[-1,:],grid.T[:-1,:]).reshape(self.shape).T
        return left_neigbors

    
if __name__=="__main__":
    life=Game_life()
    animate=True
    if animate:
        def update(frame):
            """
            Update function for the animation of the Game of Life.
            
            :param frame: The current frame number (not used directly in this case).
            :return: The grid array for updating the animation.
            """
            life.next_gen()  
            mat.set_array(life.grid)  
            return [mat]
        

        fig, ax = plt.subplots()
        mat = ax.matshow(life.grid, cmap="gray")
        ax.axis("off") 


        ani = FuncAnimation(fig, update, frames=1000, interval=1500, blit=True)

        plt.show()
    else:#For run this don't use Vscode shell, it dosen't work
        for i in range(0,10):
            #Generate a snapshot of the 10 pop
            life.next_gen()
        snap10=life.grid
        print(snap10)
        try:
            # Save the snapshot of the grid
            snap10 = life.grid
            np.save('../../test/PoP10_GameOfLife.npy', snap10)
            print("Snapshot saved successfully.")
            
        except Exception as e:
            # Print the error if there is an exception
            print(f"Error saving the file: {e}")
