import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from BicoccaCoursePython2024.seconda_lezione import Game_life

class figure():
    """
    A class to visualize planetary orbits and animate the Game of Life.
    """
    
    def __init__(self):
        """
        Initializes the figure class with data for planetary orbits and periods.
        """
        self.planet_major_ax = np.array([0.39, 0.72, 1.00, 1.52, 5.20, 9.54, 19.22, 30.06, 39.48])
        self.planet_period = np.array([0.24, 0.62, 1.00, 1.88, 11.86, 29.46, 84.01, 164.8, 248.09])
        self.planet_name = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", 
                            "Uranus", "Neptune", "Pluto"]
    
    def show_planets_orbits(self, ax=None):
        """
        Plots the period-distance relation for the Solar System planets on a log-log scale.

        Parameters:
            ax (matplotlib.axes._axes.Axes): Optional. The axes object to plot on. If None, a new figure is created.
        """
        if ax is None:
            fig, ax = plt.subplots(1, 1, figsize=(8, 8))
        
        # Plot the planetary data
        ax.plot(self.planet_major_ax, self.planet_period, linestyle='-.', marker='o')
        
        # Annotate each planet's position on the plot
        for planet, position, period in zip(self.planet_name, self.planet_major_ax, self.planet_period):
            if planet not in ['Venus', 'Mercury']:
                ax.annotate(planet,
                            xy=(position, period),  # Position to annotate
                            xytext=(position * 0.4, period),  # Offset for the text
                            arrowprops=dict(facecolor='black'),  # Arrow properties
                            horizontalalignment='left',
                            verticalalignment='bottom',
                            )
            else:
                ax.annotate(planet,
                            xy=(position, period),  # Position to annotate
                            xytext=(position * 1.4, period),  # Offset for the text
                            arrowprops=dict(facecolor='black'),  # Arrow properties
                            horizontalalignment='left',
                            verticalalignment='bottom',
                            )
        
        # Set log-log scale and labels
        ax.set_xscale('log')
        ax.set_yscale('log')
        ax.grid('both')
        ax.set_title('Period-distance relation for the Solar System')
        ax.set_xlabel('Major axes [au]')
        ax.set_ylabel("Orbit's period [yr]")
        
        plt.show()
    
    def animate_Game_of_life(self):
        """
        Creates an animation of the Game of Life using the Game_life class.

        Returns:
            matplotlib.animation.FuncAnimation: The animation object.
        """
        # Initialize the Game of Life instance
        life = Game_life()
    
        def update(frame):
            """
            Updates the Game of Life grid for each frame.

            Parameters:
                frame (int): The current frame number.
            
            Returns:
                list: Updated grid as a list.
            """
            life.next_gen()  # Compute the next generation
            mat.set_array(life.grid)  # Update the display
            return [mat]
        
        # Create a figure for the animation
        fig, ax = plt.subplots()
        mat = ax.matshow(life.grid, cmap="gray")  # Display the initial grid
        ax.axis("off")  # Remove axes for a cleaner look

        # Create the animation
        ani = FuncAnimation(fig, update, frames=1000, interval=20)

        return ani

if __name__ == "__main__":
    # Instantiate the figure class
    figure_to_show = figure()
    
    # Show planetary orbits
    figure_to_show.show_planets_orbits()
    
    # Animate the Game of Life
    ani = figure_to_show.animate_Game_of_life()

    # Display the animation
    plt.show()
