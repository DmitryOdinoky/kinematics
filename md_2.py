# inverse kinematics task



import sympy as sp
import numpy as np
from sympy import symbols
from sympy.core import Number
from IPython.display import display
import math

from scipy.optimize import fsolve

# % cosd(a1) => ca1; sind(a1) => sa1
# % cosd(a2) => ca2; sind(a2) => sa2
# % cosd(o1) => co1; sind(o1) => so1

o1, a2, ca1, sa1, ca2, sa2, co1, so1, x1, x2, x3, x4  = symbols('o1 a2 ca1 sa1 ca2 sa2 co1 so1 x1 x2 x3 x4')

#%%

# %o1=x3;
o2=math.radians(0);
o3=math.radians(0);
o4=math.radians(0);
o5=math.radians(0);
s1=490;
s2=150;
s3=700;
s4=600;
s5=250;
ai=math.radians(0);
a1_prim=math.radians(-90);
# %a2=x1;
# %a3=x2;
a4=math.radians(45);
a5=math.radians(0);


def round_expr(expr, num_digits):
    return expr.xreplace({n : round(n, num_digits) for n in expr.atoms(Number)})



    
B01 = sp.Matrix([[co1, -so1*np.cos(a1_prim), so1*np.sin(a1_prim), ai*co1],
             [so1, co1*np.cos(a1_prim), -co1*np.sin(a1_prim), ai*so1],
             [0, np.sin(a1_prim), np.cos(a1_prim), s1],
             [0, 0, 0, 1]])



B02 = sp.Matrix([[np.cos(o2), -np.sin(o2)*ca1, np.sin(o2)*sa1, ai*np.cos(o2)],
             [np.sin(o2), np.cos(o2)*ca1, -np.cos(o2)*sa1, ai*np.sin(o2)],
             [0, sa1, ca1, s2],
             [0, 0, 0, 1]])

B03 = sp.Matrix([[np.cos(o3), -np.sin(o3)*ca2, np.sin(o3)*sa2, ai*np.cos(o3)],
             [np.sin(o3), np.cos(o3)*ca2, -np.cos(o3)*sa2, ai*np.sin(o3)],
             [0, sa2, ca2, s3],
             [0, 0, 0, 1]])

B04 = sp.Matrix([[np.cos(o4), -np.sin(o4)*np.cos(a4), np.sin(o4)*sp.sin(a4), ai*np.cos(o4)],
             [np.sin(o4), np.cos(o4)*np.cos(a4), -np.cos(o4)*np.sin(a4), ai*np.sin(o4)],
             [0, np.sin(a4), np.cos(a4), s4],
             [0, 0, 0, 1]])

B05 = sp.Matrix([[np.cos(o5), -np.sin(o5)*np.cos(a5), np.sin(o5)*np.sin(a5), ai*np.cos(o5)],
             [np.sin(o5), np.cos(o5)*np.cos(a5), -np.cos(o5)*np.sin(a5), ai*np.sin(o5)],
             [0, np.sin(a5), np.cos(a5), s5],
             [0, 0, 0, 1]])

B06=B01*B02*B03*B04*B05


# B06 = B06.subs({ca1: np.cos(a1), ca2: sp.cos(a2), co1: sp.cos(o1), sa1: np.sin(a1), sa2: sp.sin(a2), so1: sp.sin(o1) })
# B06 = B06.subs({ca1: np.cos(a1), ca2: x1, co1: x2, sa1: np.sin(a1), sa2: x3, so1: x4 })
A = B06[::,-1]
# b = [900, 300, 800]




# soll = sp.nonlinsolve(A,b)

display(round_expr(A, 3))
# display(round_expr(b, 3))
# display(round_expr(B06, 3))



#%%

def func(x):

    system =[-776.776977539063*np.cos(x[0])*np.cos(x[1])*np.sin(x[2]) + 176.777008056641*np.cos(x[0])*np.sin(x[1])*np.sin(x[2]) - 700.0*np.cos(x[0])*np.sin(x[2]) + 176.777008056641*np.cos(x[1])*np.sin(x[0])*np.sin(x[2]) + 776.776977539063*np.sin(x[0])*np.sin(x[1])*np.sin(x[2]) - 150.0*np.sin(x[2]) - 900,
             776.776977539063*np.cos(x[0])*np.cos(x[1])*np.cos(x[2]) - 176.777008056641*np.cos(x[0])*np.cos(x[2])*np.sin(x[1]) + 700.0*np.cos(x[0])*np.cos(x[2]) - 176.777008056641*np.cos(x[1])*np.cos(x[2])*np.sin(x[0]) - 776.776977539063*np.cos(x[2])*np.sin(x[0])*np.sin(x[1]) + 150.0*np.cos(x[2]) - 300,
             176.777008056641*np.cos(x[0])*np.cos(x[1]) + 776.776977539063*np.cos(x[0])*np.sin(x[1]) + 776.776977539063*np.cos(x[1])*np.sin(x[0]) - 176.777008056641*np.sin(x[0])*np.sin(x[1]) + 700.0*np.sin(x[0]) + 490.0 - 800]

    return system

    
root = fsolve(func, [0, 0, 0])
    
    

print(math.degrees(root[0]))
print(math.degrees(root[1]))
print(math.degrees(root[2]))
