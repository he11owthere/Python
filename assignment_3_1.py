hrs = float(input("Enter hours: "))
rate = float(input("Enter rate: "))
if hrs <= 40:
    print(rate * hrs)
else:
    print((rate * 1.5 * (hrs-40)) + (rate * 40))