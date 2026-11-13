# ── CELL 1: Import Libraries ──────────────────────────────────────────────────
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ── CELL 2: Define the One-Variable Function ──────────────────────────────────
x = sp.Symbol('x')

# Example function — change this as needed
f = x**3 - 3*x**2 - 9*x + 5

print("Function: f(x) =", f)
# ── CELL 3: First Derivative Test — Find Critical Points ──────────────────────
f1 = sp.diff(f, x)          # First derivative f'(x)
print("First Derivative  f'(x) =", f1)

critical_points = sp.solve(f1, x)
print("Critical Points (where f'(x) = 0):", critical_points)

# ── CELL 4: Second Derivative Test — Classify Critical Points ─────────────────
f2 = sp.diff(f1, x)         # Second derivative f''(x)
print("Second Derivative f''(x) =", f2)
print()

for pt in critical_points:
    val  = f.subs(x, pt)          # Function value at critical point
    test = f2.subs(x, pt)         # f''(critical point)

    if test > 0:
        kind = "Local MINIMUM"
    elif test < 0:
        kind = "Local MAXIMUM"
    else:
        kind = "Inconclusive (test fails)"

    print(f"  x = {pt}  →  f({pt}) = {val}  →  f''= {test}  →  {kind}")