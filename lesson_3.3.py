nums = []
middle_index = len(nums) // 2
if len(nums) % 2 != 0:
    middle_index += 1
part1 = nums[:middle_index]
part2 = nums[middle_index:]
result = [part1, part2]
print(result)