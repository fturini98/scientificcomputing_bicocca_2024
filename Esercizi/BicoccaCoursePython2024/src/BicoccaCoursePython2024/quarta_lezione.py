import numpy as np
import scipy.integrate as integtate


import  scipy.signal.windows as sig
from scipy.signal import convolve

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

class units:
    G=4*np.pi
    M_sun=1


class planet():
    def __init__(self,a=1,e=0.01672,tmax=30,dt=0.007):
        
        r_p=a*(1-e)
        v_p=np.sqrt(((units.G*units.M_sun/a)*((1+e)/(1-e))))
        self.e=e #eccentricity for the planet (default=ehart)
        self.a=a#major axis in au
        self.x=r_p
        self.y=0
        self.v_x=0
        self.v_y=v_p
        
        #time step and stop time fot the integtation
        self.dt=dt
        self.tmax=tmax
        
    def motion_equations(self,t,variables):
        x,y,v_x,v_y=variables
        r=np.sqrt(x**2+y**2)
        
        dxdt=v_x
        dydt=v_y
        dv_xdt=-units.G*units.M_sun*(x/np.power(r,3))
        dv_ydt=-units.G*units.M_sun*(y/np.power(r,3))
        return np.array([dxdt,dydt,dv_xdt,dv_ydt])

    def integrate_motion_equations(self):
        
        r=integtate.solve_ivp(self.motion_equations,(0.0,self.tmax),[self.x,self.y,self.v_x,self.v_y],method="Radau", dense_output=True)
        self.time = np.arange(0.0, self.tmax, self.dt)
        
        solutions = r.sol(self.time)
        self.x_arr=solutions[0]
        self.y_arr=solutions[1]
        self.v_x_arr=solutions[2]
        self.v_y_arr=solutions[3]
    
    def animate(self):
        
        
        self.integrate_motion_equations()
        
        
        fig, ax = plt.subplots()

        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)

        ax.set_xlabel('x [au]')
        ax.set_ylabel('y [au]')
        ax.set_title('Planet\'s orbit')
        
        def update(frame):
            ax.cla()
            ax.set_xlabel('x [au]')
            ax.set_ylabel('y [au]')
            ax.set_title('Planet\'s orbit')  
            ax.set_xlim(-1.5, 1.5)  
            ax.set_ylim(-1.5, 1.5)
            ax.grid()
            ax.plot(self.x_arr[(frame-20):frame], self.y_arr[(frame-20):frame], 'r-', lw=2)  # Disegna la traiettoria aggiornata
            ax.scatter(self.x_arr[frame], self.y_arr[frame], color='blue', s=50)
            return ax,

        
        ani = FuncAnimation(fig, update, frames=len(self.time),interval=10, blit=False)
        
        return ani
    
    def animate_jnb(self):
        ani=self.animate()
        vid=HTML(ani.to_jshtml())
        return vid
        

class signal:
    def __init__(self,signal,x,std=25):
        self.std=std
        self.x=x
        self.signal=signal
    
    def clean(self):
        gaussian=sig.gaussian(len(self.signal),self.std)
        self.gaussian=gaussian
        int_gaus=np.sum(gaussian)
        self.clean_signal=convolve(self.signal,gaussian,mode='same',method='fft')/int_gaus
    
    def plot(self):
        fig,ax=plt.subplots(1,1)

        ax.plot(self.x,self.gaussian,label=rf"Gaussian filter $\sigma$={self.std}")
        ax.plot(self.x,self.signal,label="Noisy signal")
        ax.plot(self.x,self.clean_signal,label=rf"Filtered signal $\sigma$={self.std}")
        ax.legend(loc='upper left')
        return fig,ax
    
    
if __name__ == '__main__':
    Earth = planet()
    
    Earth.integrate_motion_equations()
    
    ani= Earth.animate()
    
    plt.show()
