'''
input: file of str
output: int

find letter that repeats in both halves of str
put letter into array
sum priority of each letter in array
return sum
'''
# part 1
def calculate_sum_priorites(file):
    repeated=[]
    try:
        f=open(file)
        for line in f:
            l = line.strip()
            first_half = set(l[:len(l)//2])
            second_half = set(l[len(l)//2:])

            intersection = first_half.intersection(second_half)
            repeated.append(list(intersection)[0])

    finally:
        f.close()

    sum_priorities = 0
    for c in repeated:
        if ord(c)-96 > 0:
            sum_priorities += ord(c)-96
        else:
            sum_priorities += ord(c)-38
    return sum_priorities

# part 2
'''
find repeated char in set of 3 lines
add priority of that repeated char to sum_priorities
return sum
'''
def calculate_priorites_group(file):

    sum_priorities = 0

    try:
        f=open(file)
        while True:
            l1 = set(f.readline().strip())
            l2 = set(f.readline().strip())
            l3 = set(f.readline().strip())

            if not l3: break

            intersection1 = l1.intersection(l2)
            intersection = intersection1.intersection(l3)

            c = list(intersection)[0]

            if ord(c)-96 > 0:
                sum_priorities += ord(c)-96
            else:
                sum_priorities += ord(c)-38

    finally:
        f.close()

    return sum_priorities

def main():
    print(calculate_sum_priorites("/Users/rashmisharma/Desktop/advent_of_code_22/day_3/test_3.py"))
    print(calculate_sum_priorites("/Users/rashmisharma/Desktop/advent_of_code_22/day_3/input_3.txt"))
    print(calculate_priorites_group("/Users/rashmisharma/Desktop/advent_of_code_22/day_3/test_3.py"))
    print(calculate_priorites_group("/Users/rashmisharma/Desktop/advent_of_code_22/day_3/input_3.txt"))

main()
