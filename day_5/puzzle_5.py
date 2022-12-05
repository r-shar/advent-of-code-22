'''
return string --> crates that are on top of each stack after rearranging

[
    [
        ['', 'D'], ['']
    ],
    [
        ['N', 'C'],
        ['']
    ],
    [
        ['Z', 'M', 'P'],
        ['']
    ]
]
'''
from collections import defaultdict
from collections import deque
def parse_stacks(file):

    stacks = defaultdict(list)
    num_columns = 0

    # find num columns
    with open(file) as f:
        for line in f:
            if line[0] == '1':
                columns = line.split()
                num_columns = int(columns[-1])
    # build stacks (column: stack of crates)
    with open(file) as f:

        # see top of file for structure of crates
        #crates_test
        # crates = [[[c for c in s.split(' ')] for s in x.replace('    ', ' ').replace('[', '').replace(']', '').split('\n')] for x in f if x.__contains__('[')]

        # crates_input
        crates = [[[c for c in s.split(' ')] for s in x.replace('    ', ' ').replace('            ', ' ').replace('          ', ' ').replace('[', '').replace(']', '').split('\n')] for x in f if x.__contains__('[')]

        for c in range(len(crates)-1,-1,-1):
            for b in range(len(crates[c][0])):
                if crates[c][0][b] != '':
                    stacks[b+1].append(crates[c][0][b])
    return stacks

# build a deque of lists (instructions)
# each list contains 3 ints,
    # each one representing:
        # (1) # crates to move
        # (2) from which column to move from
        # (3) which column to move to
def parse_moves(file):
    moves = deque()
    with open(file) as f:
        for line in f:
            if "move" in line:
                digits = [c for c in line.split() if c.isdigit()]
                moves.append(digits)
    return moves

# performs rearrangement procedure
# returns top of stacks

'''
while moves has more instructions:
    instruction = popleft
    num_moves = instruction[0]
    while num_moves > 0:
        crate_to_move = stacks[instruction[1]].pop
        stacks[instruction[2]].append(crate_to_move)
        num_moves -= 1

for each stack in stacks -> build str from stack.top
return str
'''
# part 1
# def find_top_of_stacks(stacks, moves):
#     tops = []
#     while moves:
#         instruction = moves.popleft()
#         num_crates = int(instruction[0])
#         from_column = int(instruction[1])
#         to_column = int(instruction[2])
#
#         while num_crates > 0:
#             crate_to_move = stacks[from_column].pop()
#             stacks[to_column].append(crate_to_move)
#             popped_crates.append(crate_to_move)
#             num_crates -= 1
#
#     for _, stack in stacks.items():
#         tops.append(stack[-1])
#
#     return "".join(tops)

# part 2
def find_top_of_stacks(stacks, moves):
    tops = []
    while moves:
        instruction = moves.popleft()
        num_crates = int(instruction[0])
        from_column = int(instruction[1])
        to_column = int(instruction[2])

        popped_crates = []
        while num_crates > 0:
            crate_to_move = stacks[from_column].pop()
            popped_crates.append(crate_to_move)
            num_crates -= 1
        while popped_crates:
            stacks[to_column].append(popped_crates.pop())

    for _, stack in stacks.items():
        tops.append(stack[-1])

    return "".join(tops)


def main():
    # stacks = parse_stacks("/Users/rashmisharma/Desktop/advent_of_code_22/day_5/test_5.txt")
    # moves = parse_moves("/Users/rashmisharma/Desktop/advent_of_code_22/day_5/test_5.txt")
    # print(find_top_of_stacks(stacks, moves))
    stacks = parse_stacks("/Users/rashmisharma/Desktop/advent_of_code_22/day_5/input_5.txt")
    moves = parse_moves("/Users/rashmisharma/Desktop/advent_of_code_22/day_5/input_5.txt")
    print(find_top_of_stacks(stacks, moves))


main()
