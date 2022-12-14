import re

hand = open('regex_sum_1446991.txt')
numlist = list()
for line in hand:
    nums = re.findall('[0-9]+', line)
    if len(nums) >= 1:
        for value in nums:
            numlist.append(value)

sum = 0
for value in numlist:
    sum = sum + int(value)

print(sum)