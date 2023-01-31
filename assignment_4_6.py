def computepay(h, r):
    if(h <= 40):
        return (h * r)
    else:
        return (((r + r/2) * (h - 40)) + (40 * r))

h = float(input("Enter hours: "))
r = float(input("Enter rate: "))
print("Pay " + str(computepay(h, r)))