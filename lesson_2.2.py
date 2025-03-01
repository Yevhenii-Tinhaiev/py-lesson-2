number = int(input('Enter a number: '))
n1 = number // 10000
n2 = number % 10000 // 1000
n3 = number % 1000 // 100
n4 = number % 100 // 10
n5 = number % 10

print(n5,n4,n3,n2,n1)
