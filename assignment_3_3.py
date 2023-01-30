score = input("Enter score: ")
try:
    x = float(score)
except:
    x = -1
if x >= 0 and x <= 1.0:
    if x >= 0.9:
        print("A")
    elif x >= 0.8:
        print("B")
    elif x >= 0.7:
        print("C")
    elif x >= 0.6:
        print("D")
    else:
        print("F")
else:
    print("Out of range")

