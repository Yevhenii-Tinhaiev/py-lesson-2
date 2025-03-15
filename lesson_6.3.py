num = int(input("Введіть число: "))
while num > 9:
    i = 1
    for digit in str(num):
        i = i * int(digit)
    num = i
print(num)