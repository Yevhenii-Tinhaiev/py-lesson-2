numbers = [0, 1, 7, 2, 4, 8]
result = sum(numbers[i] for i in range(0, len(numbers), 2)) * numbers[-1]
print(result)