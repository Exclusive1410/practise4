#n! = 1 * 2 * … * n , n! = 1 * … * (n-2) * (n-1) * n
n = int(input('Input number : '))
factorial = 1
for i in range(2, n+1):
    factorial *= i

print('Factorial of your number is = ', factorial)
