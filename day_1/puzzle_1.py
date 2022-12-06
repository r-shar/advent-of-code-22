'''
input: file with integers separated by '\n' and '\n '
output: integer

read file
sum together each int
add to list when '\n ' encountered
close file
return max calories
'''

# part 1 (find calories held by elf with max calories)
def find_elf_with_max_calories(file):
    total_calories = []
    curr_sum = 0
    try:
        f = open(file)
        for line in f:
            if line != '\n':
                calorie = int(line.strip())
                curr_sum += calorie
            else:
                total_calories.append(curr_sum)
                curr_sum = 0
    finally:
        f.close()

    return (max(total_calories))

# part 2 (find total calories carried by top three elves carrying most calories)
'''
read file
add elves' caloric sums to list (negate the values)
close file
heapify the list
return sum of first three values
'''
import heapq

def find_top_three(file):
    max_calories = []
    curr_sum = 0

    try:
        f = open(file)
        for line in f:
            if line != '\n':
                curr_sum += -(int(line.strip()))
            else:
                max_calories.append(curr_sum)
                curr_sum = 0
        if line != '\n':
            max_calories.append(-int(line.strip()))
    finally:
        f.close()

    heapq.heapify(max_calories)
    top_three_sum = 0
    for _ in range(3):
        top_three_sum += -(heapq.heappop(max_calories))

    return top_three_sum
