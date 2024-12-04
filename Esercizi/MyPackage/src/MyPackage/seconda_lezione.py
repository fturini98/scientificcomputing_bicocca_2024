import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation
class Game_life():
    def __init__(self,shape=(100,100),initial_condition="default"):
        self.grid=np.zeros(shape=shape)
        self.shape=shape
        
        if initial_condition=="default":
            self.default_initial_condition()
    
    def show(self,ax):
        ax.imshow(self.grid,cmap="gray")

    
    def default_initial_condition(self):
        y=20
        x=20
        self.grid[(0+y),(1+x)]=1
        self.grid[(1+y),(0+x):(2+x)]=1
        self.grid[(2+y),(1+x):(3+x)]=1
    
    def next_gen(self):
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
        down_neighbors=np.append(grid[1:,:],grid[0,:]).reshape(self.shape)
        return down_neighbors
    
    def shift_down(self,grid):
        up_neighbors=np.append(grid[-1,:],grid[:-1,:]).reshape(self.shape)
        return up_neighbors
    
    def shift_left(self,grid):
        right_neighbors=np.append(grid.T[1:,:],grid.T[0,:]).reshape(self.shape).T
        return right_neighbors
    
    def shift_right(self,grid):
        left_neigbors=np.append(grid.T[-1,:],grid.T[:-1,:]).reshape(self.shape).T
        return left_neigbors

    
if __name__=="__main__":
    life=Game_life()
    print('Si')
    animate=True
    if animate:
        def update(frame):
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
            # Salviamo lo snapshot della griglia
            snap10 = life.grid
            np.save('../../test/PoP10_GameOfLife.npy', snap10)
            print("Snapshot salvato correttamente.")
            
        except Exception as e:
            # Stampa l'errore se c'è un'eccezione
            print(f"Errore durante il salvataggio del file: {e}")
            