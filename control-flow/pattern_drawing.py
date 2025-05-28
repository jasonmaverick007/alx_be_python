size = int(input("Enter the size of the square: "))
i = 0
while i < size:
    for j in range(size):
        print("*", end="")
    print()
    i += 1