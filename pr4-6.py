n = int(input("Enter the width of the hourglass (odd number): "))
i = 0
while i < n:
    j = 1
    while j <= n:
        if i < j <= n - i or n - i <= j <= i + 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        j = j + 1
    print()
    i = i + 1