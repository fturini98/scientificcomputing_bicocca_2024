from numba import njit
import numpy as np
import matplotlib.pyplot as plt
import random
import bisect
import os

#===========Consistent Plot===============

def nice_plot_log(plot):
    def wrapper(self, fig, ax, max_points=1000, save=False, fig_name='fig.pdf'):
        fig, ax = plot(self, fig, ax, max_points) 
        
        ax.set_title('The Stock Market')
        ax.set_xlabel('Days')
        ax.set_ylabel('Fraction of Occourencies')
        
        ax.set_xscale('log')
        
        ax.legend(title='Market Type')
        
        if save:
            current_directory = os.getcwd()
    
    
            file_path = os.path.join(current_directory, fig_name)
            
            
            fig.savefig(file_path, format="pdf")
        
        return fig, ax 
    return wrapper

#==========The stock market================

@njit
def simulate_fast(probability_matrix, market_key, initial_state_key='Bull Market', n_days=int(1e4)):
    
    current_state = market_key.index(initial_state_key)
    probability_density_matrix = [np.cumsum(array) for array in probability_matrix]
    
    day_tracker = np.zeros(len(market_key))
    simulation_tracker = np.zeros((n_days, len(market_key)))
    
    def bisect_custom(arr, x):
        low, high = 0, len(arr)
        while low < high:
            mid = (low + high) // 2
            if arr[mid] < x:
                low = mid + 1
            else:
                high = mid
        return low
    
    for i in range(n_days):
        day_tracker[current_state] += 1
        simulation_tracker[i] = day_tracker/(i+1)
        
        density_array = probability_density_matrix[current_state]
        future_state_value = round(random.random(), 3)
        next_state = bisect_custom(density_array, future_state_value)
        
        current_state = next_state
    
    simulation_tracker = simulation_tracker.T
    return simulation_tracker


class StocK_Market_probability_matrices:
    default = np.array([[0.9, 0.025, 0.075], 
                        [0.25, 0.5, 0.25],
                        [0.15, 0.05, 0.8]] )
    
    default_keys = ['Bull Market', 'Stagnant Market', 'Bear Market']


class Stock_Market():
    
    def __init__(self, probability_matrix=StocK_Market_probability_matrices.default, market_key=StocK_Market_probability_matrices.default_keys):
        self.probability_matrix = probability_matrix
        self.market_key = market_key
    
    def choose_next_state(self):
        density_array = self.probability_density_matrix[self.current_state]
        future_state_value = round(random.random(), 3)
        return bisect.bisect_left(density_array, future_state_value)


    def simulate(self, initial_state_key='Bull Market', n_days=int(1e4)):
        self.current_state = self.market_key.index(initial_state_key)
        self.probability_density_matrix = [np.cumsum(array) for array in self.probability_matrix]
        
        day_tracker = np.zeros(len(self.market_key))
        simulation_tracker = np.zeros((n_days, len(self.market_key)))
        
        for i in range(n_days):
            day_tracker[self.current_state] += 1
            simulation_tracker[i] = day_tracker/(i+1)
            
            self.current_state = self.choose_next_state()
        
        self.simulation_tracker = np.array(simulation_tracker).T
 
    def simulate_fast(self, initial_state_key='Bull Market', n_days=int(1e4)):
        self.simulation_tracker = simulate_fast(self.probability_matrix, self.market_key, initial_state_key, n_days)

    @nice_plot_log
    def plot(self, fig , ax, max_points=1000):
        time = np.arange(len(self.simulation_tracker[0]))
        
    
        total_points = len(self.simulation_tracker[0])
        log_indices = np.unique(np.logspace(0, np.log10(total_points - 1), num=max_points, dtype=int))
        time_sampled = np.arange(total_points)[log_indices]
        
        simulation_tracker_sampled = self.simulation_tracker[:, log_indices]

        for i in range(len(simulation_tracker_sampled)):

            ax.plot(time_sampled, simulation_tracker_sampled[i], label=self.market_key[i])
            
        return fig,ax


if __name__ == '__main__':
    
    st = Stock_Market()
    
    
    st.simulate_fast(initial_state_key='Bull Market', n_days=int(1e6))

    
    fig, ax = plt.subplots(1, 1)
    
    st.plot(fig,ax,save=True)
    
    plt.show()
