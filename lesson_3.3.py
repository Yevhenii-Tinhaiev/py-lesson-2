numbers = [2, 5, 7, 8]
middle_index = len(numbers) // 2
if len(numbers) % 2 != 0:
    middle_index += 1
part1 = numbers[:middle_index]
part2 = numbers[middle_index:]
result = [part1, part2]
print(result)