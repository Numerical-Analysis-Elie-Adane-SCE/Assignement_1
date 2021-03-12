# Elie Bracha
# Adane Adgo


eps = 1.0
while eps + 1 > 1:
    eps /= 2
eps *= 2

print("The machine epsilon is:", eps)

print((abs(3.0 * (4.0 / 3.0 - 1) - 1) - eps))

print((abs(3.0 * (4.0 / 3.0 - 1) - 1)))
