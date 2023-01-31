minimum = None
maximum = None
while True:
    n = input("Enter number: ")
    try:
        n = int(n)
    except:
        if(n == "done"):
            break
        else:
            print("Invalid input")
            continue
    if minimum is None:
        minimum = n
    elif n < minimum:
        minimum = n
    if maximum is None:
        maximum = n
    elif n > maximum:
        maximum = n
print("Maximum is " + str(maximum))
print("Minimum is " + str(minimum))

    
    
