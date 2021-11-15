a = int(input('Input 1st number : '))
b = int(input('Input 2nd number : '))
c = int(input('Input 3rd number : '))
d  = int(input('Input 4th number : '))
if a > b and a > c and  a > d:
     print('Biggest number is : ', a)
elif b > a and b > c and b > d:
        print('Biggest number is : ', b)
if c > a and c > b and  c > d:
     print('Biggest number is : ', c)
elif d > a and d > b and d > c:
        print('Biggest number is : ', d)