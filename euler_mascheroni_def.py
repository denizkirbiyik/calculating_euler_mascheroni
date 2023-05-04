import decimal

inf1 = int(input("What number should be substituted for infinity in the limit for the constant definition? : "))
inf2 = int(input("What number should be substituted for infinity in the limit for the logarithm? : "))
decimal.getcontext().prec = 1 + (int(input("How many digits would you like to compute for each calculation? : ")))

def harmonic(iter):
    harmonicv = 0
    for i in range(1,iter+1):
        harmonicv += decimal.Decimal(1/i)
    return harmonicv

def log(x, inf):
    return inf*decimal.Decimal((x)**(1/inf)-1)

euler = decimal.Decimal(harmonic(inf1) - log(inf1, inf2))
print(euler)

