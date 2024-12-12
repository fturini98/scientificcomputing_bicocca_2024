import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from BicoccaCoursePython2024.seconda_lezione import Game_life
class figure():
    
    def __init__(self):
        self.planet_major_ax= np.array([0.39, 0.72, 1.00, 1.52, 5.20, 9.54, 19.22, 30.06, 39.48])
        self.planet_period=np.array([0.24, 0.62, 1.00, 1.88, 11.86, 29.46, 84.01, 164.8, 248.09])
        self.planet_name=["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", 
         "Uranus", "Neptune", "Pluto"]
    
    def show_planets_orbits(self,ax=None):
        if ax is None:
            fig,ax=plt.subplots(1,1,figsize=(8,8))
            
        ax.plot(self.planet_major_ax,self.planet_period,linestyle='-.',marker='o')
        
        for planet,position,period in zip(self.planet_name,self.planet_major_ax,self.planet_period):
            if planet not in ['Venus','Mercury']:
                ax.annotate(planet,
                xy=(position, period),  # theta, radius
                xytext=(position*0.4, period),    
                arrowprops=dict(facecolor='black'),
                horizontalalignment='left',
                verticalalignment='bottom',
                )
            else:
                ax.annotate(planet,
                xy=(position, period),  # theta, radius
                xytext=(position*1.4, period),    
                arrowprops=dict(facecolor='black'),
                horizontalalignment='left',
                verticalalignment='bottom',
                )

        
        ax.set_xscale('log')
        ax.set_yscale('log')
        ax.grid('both')
        ax.set_title('Period-distance relation for the Solar system')
        ax.set_xlabel('Major axes [au]')
        ax.set_ylabel('Orbit\'s eriod [yr]')
        
        plt.show()
    
    def animate_Game_of_life(self):
        life=Game_life()
    
        def update(frame):
            life.next_gen()  
            mat.set_array(life.grid)  
            return [mat]
        
        
        fig, ax = plt.subplots()
        mat = ax.matshow(life.grid, cmap="gray")
        ax.axis("off")  

        
        ani = FuncAnimation(fig, update, frames=1000, interval=20)

        return ani

if __name__=="__main__":
    figure_to_show=figure()
    
    figure_to_show.show_planets_orbits()
    
    ani=figure_to_show.animate_Game_of_life()

    plt.show()