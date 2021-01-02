import numpy as np
import sympy as sp
import matplotlib
# matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline






# Interpolation tasks:
# Newton formula (Forward/backward):
def newton_interp_1(x, x_values, y_values, h, forward=True):
    """
    :param x: symbolic x in formula
    :param x_values: steps for in between points
    :param y_values: in between point values for y axis
    :param h: step size
    :param forward: boolean operator for checking if using forward difference or backward
        defaults to forward, pass 'False' for backward interpolation.
    :return: Newton polynomial for interpolation
    """

    # Define U and polynomial start based on mode:
    if forward:
        U = (x - x_values[0]) / h
        top = None
        P = y_values[0]
    else:
        U = (x - x_values[-1]) / h
        top = None
        P = y_values[-1]

    # Calculate each step for getting values:
    for i in range(1, len(x_values), 1):

        # Calculate difference between elements and set y_values to new difference for calculating it forwards:
        y_prev = y_values[:-1]
        y_next = y_values[1:]
        y_diff = y_next - y_prev
        # Print values for debugging:
        print(y_diff)
        y_values = y_diff

        # Set y_value, increase U and calculate addition:
        if forward:
            y_ord_diff = y_values[0]
        else:
            y_ord_diff = y_values[-1]

        # When 1st time, U is already set. If check to avoid extra editing).
        if i == 1:
            top = U
        else:
            # Check if forward/backward and adjust:
            if forward:
                top *= U - i + 1
            else:
                top *= U + i - 1

        P += (top / np.math.factorial(i)) * y_ord_diff

    # Return gotten polynomial:
    return P


# Function for getting interpolation result graph array:
def build_interp_line(p, s, e, h):

    # Create dummy array:
    dummy = np.linspace(s, e, h)
    result = []

    # Iterate over dummy array, get data points and create an array for gotten line:
    for i in dummy:

        point = p.subs(x, i)
        result.append(point)

    return np.asarray(result)


# Define necessary variables and values for getting polynomial for interpolation:
x = sp.Symbol('x')
x_values_1 = np.arange(3, 13, 1)
y_values_1 = np.array([15.8,19.8,21.2,22,22,21.7,20.8,19,16.2,11])
x_values_2 = np.arange(4, 13, 2)
y_values_2 = np.array([19.8, 22, 21.7, 19, 11])







P_1 = newton_interp_1(x, x_values_1, y_values_1, 1)
print("\n", P_1)
print("\n", sp.simplify(P_1))

P_2 = newton_interp_1(x, x_values_2, y_values_2, 2)
print("\n", P_2)
print("\n", sp.simplify(P_2))

P_3 = newton_interp_1(x, x_values_1, y_values_1, 1, forward=False)
print("Backward polynomial: \n", sp.simplify(P_3))
P_4 = newton_interp_1(x, x_values_2, y_values_2, 2, forward=False)
print("Backward polynomial: \n", sp.simplify(P_4))

# Hand-crafted polynomial (fairly close to real values, good job Matīss, well solved, mostly rounding errors):
P_hand = 1151.6427 - 2993.581 * x + 2100.0503 * x ** 2 - 1333.862 * x ** 3 + 443.9462 * x ** 4 - 95.6075 * x ** 2 \
    + 14.582 * x ** 6 - 1.544 * x ** 7 + 0.122 * x ** 8 - 0.052 * x ** 9 + 0.000143 * x ** 10 - 1.736e-6 * x ** 11

# Control values for polynomial error check:
P_1_check = np.array([P_1.subs(x, 2), P_1.subs(x, 3), P_1.subs(x, 4), P_1.subs(x, 5), P_1.subs(x, 6), P_1.subs(x, 7),
                      P_1.subs(x, 8), P_1.subs(x, 9), P_1.subs(x, 10), P_1.subs(x, 11)
                      ])

P_2_check = np.array([P_2.subs(x, 2), P_2.subs(x, 4), P_2.subs(x, 6), P_2.subs(x, 8), P_2.subs(x, 10)])

P_1_error = np.abs(P_1_check - y_values_1)
P_2_error = np.abs(P_2_check - y_values_2)
P_1_total_error = np.mean(P_1_error)
P_2_total_error = np.mean(P_2_error)
print("Control values: \n", P_1_check, "\n Error values: \n", P_1_error, "\t mean: ", P_1_total_error)
print("Control values: \n", P_2_check, "\n Error values: \n", P_2_error, "\t mean: ", P_2_total_error)

# Cubic spline using SciPy:
P_spline = CubicSpline(x_values_1, y_values_1)
P_spline_2 = CubicSpline(x_values_2, y_values_2)

s, e, h = 2, 13, 100
x_axis = np.linspace(s, e, h)
# Build interpolation line:
interp_line_1 = build_interp_line(P_1, s, e, h)
interp_line_2 = build_interp_line(P_2, s, e, h)
interp_line_3 = build_interp_line(P_3, s, e, h)
interp_line_4 = build_interp_line(P_4, s, e, h)
interp_line_hand = build_interp_line(P_hand, s, e, h)

cub_spline_interp = P_spline_2(np.linspace(s, e, h))

# 10 point interpolation for 1st formula:
# plt.figure()
# plt.title("Interpolācija 10 punktiem, h = 1 (1. formula)")
# plt.plot(np.linspace(s, e, h), interp_line_1, '-b', label="Līnija")
# plt.plot(x_values_1, y_values_1, 'g.', label="Punkti")
# plt.grid()
# plt.legend()
# plt.show()
# plt.pause(1)

# # 5 point interpolation for 1st formula:

plt.title("Interpolācija 5 punktiem, h = 2 (Ņūtona)")
plt.plot(np.linspace(s, e, h), interp_line_2, '--b', label="Līnija")
plt.plot(x_values_2, y_values_2, 'go', label="Punkti")
plt.ylim(0,25)

plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

plt.grid()
plt.legend()
plt.show()


plt.title("Interpolācija 5 punktiem, h = 2 (Kubiskie splaini)")
plt.plot(np.linspace(s, e, h), P_spline_2(np.linspace(s, e, h)), '--b', label="Līnija")
plt.plot(x_values_2, y_values_2, 'go', label="Punkti")
plt.ylim(0,25)

plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

plt.grid()
plt.legend()
plt.show()


# 10 point interpolation for 2nd formula:

plt.title("Interpolācija 10 punktiem, h = 1 (Ņūtona)")
plt.plot(np.linspace(s, e, h), interp_line_3, '--b', label="Līnija")
plt.plot(x_values_1, y_values_1, 'go', label="Punkti")
plt.ylim(0,25)

plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

plt.grid()
plt.legend()
plt.show()

# 10 point interpolation, Splines:

plt.title("Interpolācija 10 punktiem, h = 1 (Kubiskie splaini)")
plt.plot(np.linspace(s, e, h), P_spline(np.linspace(s, e, h)), '--b', label="Līnija")
plt.plot(x_values_1, y_values_1, 'go', label="Punkti")
plt.ylim(0,25)

plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

plt.grid()
plt.legend()
plt.show()


# # 5 point interpolation for 2nd formula:

# plt.title("Interpolācija 5 punktiem, h = 2 (2. formula)")
# plt.plot(np.linspace(s, e, h), interp_line_4, '--b', label="Līnija")
# plt.plot(x_values_2, y_values_2, 'g.', label="Punkti")
# plt.grid()
# plt.legend()
# plt.show()


# # Cubic spline for comparison with 10 point interpolation:

# plt.title("Interpolācija 10 punktiem, h = 1 (Kubiskie splaini)")
# plt.plot(np.linspace(s, e, h), P_spline(np.linspace(s, e, h)), '--b', label="Līnija")
# plt.plot(x_values_1, y_values_1, 'g.', label="Punkti")
# plt.grid()
# plt.legend()
# plt.show()

