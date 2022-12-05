'''
input: text file with pairs of int ranges
output: int

remove non-numbers
[a,b][c,d]

[c,d] overlaps [a,b]
[a,b] overlaps [c,d]

a <= c <= d <= b
c <= a <= b <= d
'''

# part 1
def count_overlap(file):
    num_overlaps = 0
    lines = []
    with open(file) as f:
        lines = [[[int(i) for i in range.split("-")] for range in x.split(",")] for x in f]
    num_overlaps += sum(a <= c <= d <= b or c <= a <= b <= d for (a,b), (c,d) in lines)

    return num_overlaps

# part 2
def count_overlap_2(file):
    num_overlaps = 0
    lines = []
    with open(file) as f:
        lines = [[[int(i) for i in range.split("-")] for range in x.split(",")] for x in f]
    num_overlaps += sum(a <= d and  b >= c for (a,b), (c,d) in lines)

    return num_overlaps
def main():
    print(count_overlap("/Users/rashmisharma/Desktop/advent_of_code_22/day_4/test_4.txt"))
    print(count_overlap_2("/Users/rashmisharma/Desktop/advent_of_code_22/day_4/input_4.txt"))
#
main()
