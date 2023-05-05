import decimal

iter = int(input("How many terms of the series should be calculated? : "))
inf1 = int(input("What number should be substituted for infinity in the limit for the logarithm?(Can be relatively low.) : "))
decimal.getcontext().prec = 1 + (int(input("How many digits would you like to compute for each calculation? : ")))

def log2(x, inf):
    return decimal.Decimal((x)**(1/inf)-1)/decimal.Decimal((2)**(1/inf)-1)

def vacca_sum(iter, inf):
    sum = 0
    for i in range(2,iter):
        sum += ((-1)**i)*decimal.Decimal((log2(i, inf)).__floor__())*decimal.Decimal(1/i)
    return sum

euler = vacca_sum(iter, inf1)
print(euler)