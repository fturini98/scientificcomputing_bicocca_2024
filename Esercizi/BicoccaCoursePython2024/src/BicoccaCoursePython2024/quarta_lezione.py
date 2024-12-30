import numpy as np
import scipy.integrate as integrate
import scipy.signal.windows as sig
from scipy.signal import convolve

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

class units:
    """
    A utility class to define constants used in planetary simulations.
    """
    G = 4 * np.pi  # Gravitational constant (in astronomical units)
    M_sun = 1      # Mass of the Sun (normalized to 1)

class planet():
    """
    A class to simulate and animate the motion of a planet around a star using Keplerian dynamics.
    """

    def __init__(self, a=1, e=0.01672, tmax=30, dt=0.05):
        """
        Initializes the planet with orbital parameters and initial conditions.

        Parameters:
            a (float): Semi-major axis in AU (default: 1, Earth's orbit).
            e (float): Orbital eccentricity (default: 0.01672, Earth's eccentricity).
            tmax (float): Maximum simulation time in years (default: 30).
            dt (float): Time step for the integration (default: 0.05).
        """
        # Orbital parameters
        r_p = a * (1 - e)  # Perihelion distance
        v_p = np.sqrt((units.G * units.M_sun / a) * ((1 + e) / (1 - e)))  # Perihelion velocity

        self.e = e  # Orbital eccentricity
        self.a = a  # Semi-major axis
        self.x = r_p
        self.y = 0
        self.v_x = 0
        self.v_y = v_p

        # Simulation parameters
        self.dt = dt
        self.tmax = tmax

    def motion_equations(self, t, variables):
        """
        Defines the equations of motion for the planet under gravitational attraction.

        Parameters:
            t (float): Time (unused as the equations are time-independent).
            variables (list): State vector [x, y, v_x, v_y].

        Returns:
            np.array: Derivatives [dx/dt, dy/dt, dv_x/dt, dv_y/dt].
        """
        x, y, v_x, v_y = variables
        r = np.sqrt(x**2 + y**2)  # Distance from the central body

        # Equations of motion
        dxdt = v_x
        dydt = v_y
        dv_xdt = -units.G * units.M_sun * (x / r**3)
        dv_ydt = -units.G * units.M_sun * (y / r**3)
        return np.array([dxdt, dydt, dv_xdt, dv_ydt])

    def integrate_motion_equations(self):
        """
        Integrates the equations of motion using the `solve_ivp` method.
        """
        # Integrate motion equations over time
        result = integrate.solve_ivp(
            self.motion_equations,
            (0.0, self.tmax),
            [self.x, self.y, self.v_x, self.v_y],
            method="Radau",
            dense_output=True
        )
        # Time array for sampling
        self.time = np.arange(0.0, self.tmax, self.dt)

        # Extract solutions for position and velocity
        solutions = result.sol(self.time)
        self.x_arr = solutions[0]
        self.y_arr = solutions[1]
        self.v_x_arr = solutions[2]
        self.v_y_arr = solutions[3]

    def animate(self):
        """
        Animates the planet's orbit using Matplotlib.

        Returns:
            matplotlib.animation.FuncAnimation: Animation object for the orbit.
        """
        self.integrate_motion_equations()  # Ensure motion equations are integrated

        # Set up the figure and axes for the animation
        fig, ax = plt.subplots()
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.set_xlabel('x [au]')
        ax.set_ylabel('y [au]')
        ax.set_title("Planet's orbit")

        def update(frame):
            """
            Updates the animation frame by frame.

            Parameters:
                frame (int): The current frame index.

            Returns:
                matplotlib.axes._axes.Axes: Updated axis.
            """
            ax.cla()
            ax.set_xlabel('x [au]')
            ax.set_ylabel('y [au]')
            ax.set_title("Planet's orbit")
            ax.set_xlim(-1.5, 1.5)
            ax.set_ylim(-1.5, 1.5)
            ax.grid()

            # Plot the trajectory and the current position of the planet
            ax.plot(self.x_arr[max(0, frame - 5):frame], self.y_arr[max(0, frame - 5):frame], 'r-', lw=2)
            ax.scatter(self.x_arr[frame], self.y_arr[frame], color='blue', s=50)
            return ax,

        # Create the animation
        ani = FuncAnimation(fig, update, frames=len(self.time), interval=50, blit=False)
        return ani

    def animate_jnb(self):
        """
        Creates an animation for use in Jupyter Notebooks.

        Returns:
            IPython.display.HTML: HTML representation of the animation.
        """
        ani = self.animate()
        vid = HTML(ani.to_jshtml())
        return vid

class signal:
    """
    A class to process and filter noisy signals using convolution with a Gaussian filter.
    """

    def __init__(self, signal, x, std=25):
        """
        Initializes the signal processing class.

        Parameters:
            signal (np.array): The noisy signal to be filtered.
            x (np.array): The x-values corresponding to the signal.
            std (int): Standard deviation of the Gaussian filter (default: 25).
        """
        self.std = std
        self.x = x
        self.signal = signal

    def clean(self):
        """
        Filters the noisy signal using a Gaussian filter.
        """
        gaussian = sig.gaussian(len(self.signal), self.std)
        self.gaussian = gaussian
        int_gaus = np.sum(gaussian)
        self.clean_signal = convolve(self.signal, gaussian, mode='same', method='fft') / int_gaus

    def plot(self):
        """
        Plots the original signal, the Gaussian filter, and the filtered signal.

        Returns:
            tuple: (fig, ax) The figure and axes of the plot.
        """
        fig, ax = plt.subplots(1, 1)
        ax.plot(self.x, self.gaussian, label=rf"Gaussian filter $\sigma$={self.std}")
        ax.plot(self.x, self.signal, label="Noisy signal")
        ax.plot(self.x, self.clean_signal, label=rf"Filtered signal $\sigma$={self.std}")
        ax.legend(loc='upper left')
        return fig, ax

if __name__ == '__main__':
    # Example usage: simulate Earth's orbit
    Earth = planet()
    Earth.integrate_motion_equations()
    ani = Earth.animate()
    plt.show()
