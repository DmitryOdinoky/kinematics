# forward kinematics task

import sympy as sp
import numpy as np
from sympy.physics.mechanics import dynamicsymbols
from sympy.core import Number
from IPython.display import display
import math

theta, S, a, alpha = dynamicsymbols('theta S a alpha')
#%%

def round_expr(expr, num_digits):
    return expr.xreplace({n : round(n, num_digits) for n in expr.atoms(Number)})


def transformation():
    
    B = sp.Matrix([[sp.cos(theta), -sp.sin(theta)*sp.cos(alpha), sp.sin(theta)*sp.sin(alpha), a*sp.cos(theta)],
                 [sp.sin(theta), sp.cos(theta)*sp.cos(alpha), -sp.cos(theta)*sp.sin(alpha), a*sp.sin(theta)],
                 [0, sp.sin(alpha), sp.cos(alpha), S],
                 [0, 0, 0, 1]])
    
    
    
    return B


#%%

print('B01:' + '\n')

B01 = transformation()

display(B01)

B01 = sp.N(B01.subs({theta: math.radians(-90-30), alpha: math.radians(-90), a: 0, S: 490}))



display(round_expr(B01, 3))
print('\n')

#%%

B02 = transformation()
display(B02)
B02 = sp.N(B02.subs({theta: math.radians(0), alpha: math.radians(90-(-60)), a: 0, S: 150}))


print('B02:' + '\n')
display(round_expr(B02, 3))
print('\n')

#%%

B03 = transformation()
display(B03)
B03 = sp.N(B03.subs({theta: math.radians(0), alpha: math.radians(-90-(+60)), a: 0, S: 700}))


print('B03:' + '\n')
display(round_expr(B03, 3))
print('\n')

#%%

B04 = transformation()
display(B04)
B04 = sp.N(B04.subs({theta: math.radians(0), alpha: math.radians(0-(+45)), a: 0, S: 600}))


print('B04:' + '\n')
display(round_expr(B04, 3))
print('\n')



#%%

B05 = transformation()
display(B05)
B05 = sp.N(B05.subs({theta: math.radians(0), alpha: math.radians(0), a: 0, S: 250}))


print('B05:' + '\n')
display(round_expr(B05, 3))
print('\n')

#%%

B6 = B01*B02*B03*B04*B05
display(B6)

# B6 = B05


print('RESUT, B6:' + '\n')
display(round_expr(B6, 3))
print('\n')

#%%


# def transformation_2():
    
#     B = sp.Matrix([[sp.cos(theta)]],
#                  )
    
    
    
#     return B

# B_test = transformation_2()
# B_test = sp.N(B_test.subs({theta: 0}))


# print('B_test:' + '\n')
# display(B_test)
# print('\n')
