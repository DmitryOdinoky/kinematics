import numpy as np
import sympy as sym


# Tripod parallel robot:

# Forward kinematics:
Az, Bz, Cz = 29, 30, 31
L = 19.5
Hcz = 0
S = 30
Se = 15
Avx, Avy = 0, 9.99
Bvx, Bvy = 8.65, -4.995
Cvx, Cvy = -8.65, -4.995

x_0, y_0, z_0 = sym.symbols('x0 y0 z0')

eq_1 = sym.Eq((Az - Hcz - z_0) ** 2, L ** 2 - (x_0 - Avx) ** 2 - (y_0 - Avy) ** 2)
eq_2 = sym.Eq((Bz - Hcz - z_0) ** 2, L ** 2 - (x_0 - Bvx) ** 2 - (y_0 - Bvy) ** 2)
eq_3 = sym.Eq((Cz - Hcz - z_0) ** 2, L ** 2 - (x_0 - Cvx) ** 2 - (y_0 - Cvy) ** 2)

roots_forward = sym.solve([eq_1, eq_2, eq_3], [x_0, y_0, z_0], dict=True)
# roots_forward = sym.nsolve([eq_1, eq_2, eq_3], [x_0, y_0, z_0],[0,0,0])
print("Result \n", roots_forward)

#%%

# Inverse kinematics:

root_index = 0    
    
X, Y, Z = roots_forward[root_index][list(roots_forward[root_index].keys())[0]], roots_forward[root_index][list(roots_forward[root_index].keys())[1]], roots_forward[root_index][list(roots_forward[root_index].keys())[2]]
A_z, B_z, C_z = sym.symbols('Az Bz Cz')

eq_4 = sym.Eq((A_z - Hcz - Z) ** 2, L ** 2 - (X - Avx) ** 2 - (Y - Avy) ** 2)
eq_5 = sym.Eq((B_z - Hcz - Z) ** 2, L ** 2 - (X - Bvx) ** 2 - (Y - Bvy) ** 2)
eq_6 = sym.Eq((C_z - Hcz - Z) ** 2, L ** 2 - (X - Cvx) ** 2 - (Y - Cvy) ** 2)

roots_inverse = sym.solve([eq_4, eq_5, eq_6], [A_z, B_z, C_z], dict=True)
# roots_inverse = sym.nsolve([eq_1, eq_2, eq_3], [x_0, y_0, z_0],[0,0,0])
print("Result \n", roots_inverse[root_index-1])