import numpy as np
import sympy as sym
import math
from scipy.optimize import fsolve

theta1 = math.radians(15)
theta2 = math.radians(45)
theta3 = math.radians(15)

J1 = [0, -(44.5-17.5)/(2*np.sqrt(3))+27*np.cos(theta1), -27*np.sin(theta1)]
J2 = [((44.5-17.5)/2*np.sqrt(3)+27*np.cos(theta2))*np.cos(math.radians(30)), ((44.5-17.5)/2*np.sqrt(3)+27*np.cos(theta2)*np.sin(math.radians(30))), -27*np.sin(theta2)]
J3 = [-((44.5-17.5)/2*np.sqrt(3)+27*np.cos(theta3))*np.cos(math.radians(30)), ((44.5-17.5)/2*np.sqrt(3)+27*np.cos(theta3)*np.sin(math.radians(30))), -27*np.sin(theta3)]

#%%

def func(x):

    system =[(x[0] - 0)**2 + (x[1]- (18.28))**2 + (x[2]-(-6.99))**2 - 47**2,
             (x[0] - 36.78)**2 + (x[1]- (32.93))**2 + (x[2]-(-19.09))**2 - 47**2,
             (x[0] - (-42.83))**2 + (x[1]- (36.42))**2 + (x[2]-(-6.99))**2 - 47**2]

    return system

    
root = fsolve(func, [0, 0, 0])


#%%

# x_0, y_0, z_0 = sym.symbols('x0 y0 z0')

# eq_1 = sym.Eq((47.5) ** 2, (x_0 - 0) ** 2  + (y_0 - (-52.46))**2 + (z_0 - (-13.5))**2)
# eq_2 = sym.Eq((47.5) ** 2, (x_0 - 29.48) ** 2  + (y_0 - 17.02)**2 + (z_0 - (-6.3))**2)
# eq_3 = sym.Eq((47.5) ** 2, (x_0 - 15.99) ** 2  + (y_0 - 17.)**2 + (z_0 - (-13.5))**2)

# ans = sym.solve([eq_1, eq_2, eq_3], [x_0, y_0, z_0], dict=True)
# print("Result \n", ans)









#%%


