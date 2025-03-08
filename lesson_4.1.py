numbers = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
i = 0
for item in numbers:
    if item != 0:
        numbers[i] = item
        i += 1
while i < len(numbers):
    numbers[i] = 0
    i += 1
print(numbers)