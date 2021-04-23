# Simplify the result of 2d_cylinder_in_3d.py.
# Please run it in Ipython, using "ipython simplify.py".
# Use "diff simplified_result.txt sympy_result.txt" in Bash to compare results.

from sympy import *

with open('sympy_result.txt', 'r') as f:
    result = sympify(f.read())

# Warning: this will take a lot of time.
simplified_result = simplify(result)

with open('simplified_result.txt', 'w') as f:
    f.write(str(simplified_result))
