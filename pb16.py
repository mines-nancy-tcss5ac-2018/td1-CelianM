def solve16(n):
    "Solve the 16th Euler problem, n : int -> sum of the digits of 2**n"
    sum = 0
    power = 2**n
    while power > 0:
        sum += power % 10
        power = power //10
    return sum

assert(solve16(15) == 26)

print("La solution du 16ème problème d'Euler est", solve16(1000))
