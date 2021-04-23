# Calculate a necessary condition where a 3d smooth curve is on a 2d cylinder.
# Please run it in Ipython, using "ipython 2d_cylinder_in_3d.py".

from sympy import *

s = Symbol('s')

for v1 in ('r', 't', 'n', 'b'):
    for v2 in ('r', 't', 'n', 'b'):
        exec(f"p{v1}{v2}=Function('p{v1}{v2}')(s)")

K, T = Function('K')(s), Function('T')(s)

equ = {
    Derivative(prt,s): ptt+K*prn,
    Derivative(prn,s): ptn-K*prt+T*prb,
    Derivative(prb,s): ptb-T*prn,
    Derivative(ptt,s): 2*K*ptn,
    Derivative(ptn,s): K*pnn-K*ptt+T*ptb,
    Derivative(ptb,s): K*pnb-T*ptn,
    Derivative(pnn,s): -2*K*ptn+2*T*pnb,
    Derivative(pnb,s): -K*ptb+T*pbb-T*pnn,
    Derivative(pbb,s): -2*T*pnb
}

exprs = []

expr = prt
exprs.append(expr)

for _ in range(8):
    expr = simplify(diff(expr).subs(equ))
    exprs.append(expr)

subs_0 = {
    prt: 0,
    prn: 0,
    prb: 0,
    ptt: 0,
    ptn: 0,
    ptb: 0,
    pnn: 0,
    pnb: 0,
    pbb: 0
}
mat = []
for i in range(9):
    mat.append([])
    for expr in subs_0.keys():
        subs = subs_0.copy()
        subs[expr] = 1
        mat[i].append(exprs[i].subs(subs))

# Warning: this will take a lot of time.
result = Matrix(mat).det()

with open('sympy_result.txt', 'w') as f:
    f.write(str(result))
