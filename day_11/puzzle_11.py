'''
input:
 - Monkey number
    - starting worry
    - how worry increases
    - test
        - if true -> monkey number
        - if false -> monkey number

* before testing worry level, worry level is divided by three (rounded down)
* a turn (round) consists of a single monkey inspecting and throwing
    all items it is holding one at a time in order listed
* when item thrown to monkey, item goes to end of recipient's list


output:
* find two monkeys with highest num of inspected items
* multiply their numbers together and return
'''
from collections import defaultdict, deque
import heapq
import math

monkey_items = defaultdict(list)
monkey_operation = defaultdict(str)
monkey_test = defaultdict(int)
monkey_actions = defaultdict(list)
num_inspected = defaultdict(int)
monkey_num = 0

def find_monkey_business(file):

    round = 0

    with open(file) as f:
        for line in f:

            l = line.strip()
            if l != '':
                if l[0] == 'M':
                    monkey_num = [int(x) for x in l if x.isdigit()][0]

                elif l[0] == 'S':
                    worries = deque([int(x) for x in l.replace(',', '').split() if x.isdigit()])
                    monkey_items[monkey_num] = worries

                elif l[0] == 'O':
                    operation = l.replace("Operation: ", '')
                    monkey_operation[monkey_num] = operation

                elif l[0] == 'T':
                    test = [int(x) for x in l.split() if x.isdigit()][0]
                    monkey_test[monkey_num] = test

                elif "true" in l:
                    true_pass = [int(x) for x in l.split() if x.isdigit()]
                    monkey_actions[monkey_num] = true_pass

                else:
                    false_pass = [int(x) for x in l.split() if x.isdigit()][0]
                    monkey_actions[monkey_num].append(false_pass)

    num_monkeys = monkey_num

    # part 2
    mod_by = math.prod([v for v in monkey_test.values()])

    for _ in range(10000):
        monkey_num = 0
        while monkey_num <= num_monkeys:
            while monkey_items[monkey_num]:
                # get item, divide by three
                item = monkey_items[monkey_num].popleft()

                # calculate new item based on operation
                operation = monkey_operation[monkey_num]
                operation_parts = [x for x in operation.split()]
                op, num = operation_parts[3], operation_parts[4]

                if num.isdigit():
                    if op == '*':
                        item *= int(num)
                    elif op == '+':
                        item += int(num)
                else:
                    if op == '*':
                        item *= item
                    elif op == '+':
                        item += item

                # divide by three (part 1)
                # item //= 3

                num_inspected[monkey_num] -= 1

                # run test
                # throw to correct monkey based on test result
                test = monkey_test[monkey_num]

                item %= mod_by

                if item % test == 0:
                    true_monkey = monkey_actions[monkey_num][0]
                    monkey_items[true_monkey].append(item)
                else:
                    false_monkey = monkey_actions[monkey_num][1]
                    monkey_items[false_monkey].append(item)

            monkey_num += 1

    # find top two monkeys and calculate monkey business
    heap = [num_inspections for num_inspections in num_inspected.values()]
    heapq.heapify(heap)

    business = 1
    for _ in range(2):
        business *= (-1*(heapq.heappop(heap)))

    print(business)
