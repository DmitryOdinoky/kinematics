import numpy as np
# import sympy as sym
from sympy import *
import math
from math import radians
from scipy.optimize import fsolve


rf = 27
re = 47.5
f = 44.5
e = 17.5

theta1 = math.radians(15)
theta2 = math.radians(45)
theta3 = math.radians(15)

# theta1 = 30
# theta2 = 15
# theta3 = 15

J1 = [0, -(f-e)/(2*np.sqrt(3))+rf*np.cos(theta1), -rf*np.sin(theta1)]
J2 = [((f-e)/(2*np.sqrt(3))+rf*np.cos(theta2))*np.cos(math.radians(30)), ((f-e)/(2*np.sqrt(3))+rf*np.cos(theta2))*np.sin(math.radians(30)), -rf*np.sin(theta2)]
J3 = [(-(f-e)/(2*np.sqrt(3))+rf*np.cos(theta3))*np.cos(math.radians(30)), ((f-e)/(2*np.sqrt(3))+rf*np.cos(theta3))*np.sin(math.radians(30)), -rf*np.sin(theta3)]


print(J1)
print(J2)
print(J3)
#%%

x, y, z = symbols('x, y, z')

forward_roots = nsolve([Eq((x - J1[0])**2 + (y- J1[1])**2 + (z-J1[2])**2 - re**2, 0),
                        Eq((x - J2[0])**2 + (y- J2[1])**2 + (z-J2[2])**2 - re**2, 0),
                        Eq((x - J3[0])**2 + (y- J3[1])**2 + (z-J3[2])**2 - re**2, 0)], 
                       [x, y, z], 
                       [0, 0, 0])

print('\n')
print(forward_roots[0])
print(forward_roots[1])
print(forward_roots[2])



#%%

x = forward_roots[0]
y = forward_roots[1]
z = forward_roots[2]

# o1 = 30
# o2 = 15
# o3 = 15
o1, o2, o3 = symbols('o1, o2, o3')

inverse_roots = nsolve([Eq((x - 0) ** 2 + (y - (-(f - e) / (2 * sqrt(3)) + rf * cos(o1))) ** 2 + (z - (- rf * sin(o1))) ** 2 - re ** 2, 0),
        Eq((x - (((f - e) / (2 * sqrt(3)) + rf * cos(o2)) * cos(radians(30)))) ** 2 + (y - (((f - e) / (2 * sqrt(3)) + rf * cos((o2))) * sin(radians(30)))) ** 2 + (z - (- rf * sin((o2)))) ** 2 - re ** 2, 0),
        Eq((x - ((-(f - e) / (2 * sqrt(3)) + rf * cos((o3))) * cos(radians(30)))) ** 2 + (y - (((f - e) / (2 * sqrt(3)) + rf * cos((o3))) * sin(radians(30)))) ** 2 + (z - (- rf * sin((o3)))) ** 2 - re ** 2, 0)], [o1, o2, o3], [0, 0, 0])

print('\n')
print(math.degrees(inverse_roots[0]))
print(math.degrees(inverse_roots[1]))
print(math.degrees(inverse_roots[2]))