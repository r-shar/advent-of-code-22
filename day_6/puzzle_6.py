'''
input: string of lowercase chars
output: int

sliding window, hashmap

- iterate over input
    - increment map[curr_char]
    - while map[curr_char] > 1
        - decrement input[start]
        - slide window forward
    - if end-start+1 == 4
        - return end+1
'''
from collections import defaultdict

# part 1
def calculate_start_of_packet(file):
    buffer = None
    with open(file) as f:
        buffer = f.read().strip('\n')

    seen = defaultdict(int)
    start = 0

    for end in range(len(buffer)):
        seen[buffer[end]] += 1

        while seen[buffer[end]] > 1:
            seen[buffer[start]] -= 1
            start += 1

        if end-start+1 == 4:
            return end + 1

# part 2
def calculate_start_of_message(file):
    buffer = None
    with open(file) as f:
        buffer = f.read().strip('\n')

    seen = defaultdict(int)
    start = 0

    for end in range(len(buffer)):
        seen[buffer[end]] += 1

        while seen[buffer[end]] > 1:
            seen[buffer[start]] -= 1
            start += 1

        if end-start+1 == 14:
            return end + 1
