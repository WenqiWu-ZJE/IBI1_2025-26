# 4.1 Population data
a = 5.08
b = 5.33
c = 5.55
d = b - a
e = c - b
print("Difference 2004-2014:", d)
print("Difference 2014-2024:", e)
print("Is population growth accelerating?", d < e)
# Since d (0.25) is greater than e (0.22), the population growth in Scotland is decelerating.

# 4.2 Booleans
X = True
Y = False
W = X or Y
print("X or Y is ", W)
# --- Truth Table for W (X or Y) ---
# X      | Y      | W (X or Y)
# ---------------------------
# True   | True   | True
# True   | False  | True
# False  | True   | True
# False  | False  | False