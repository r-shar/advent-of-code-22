#part 1
from collections import defaultdict

def find_sum(file):
    instructions = None
    with open(file) as f:
        instructions = [[x for x in line.split(' ')] for line in f.read().strip().split('\n')]

    x = 1
    cycle = 1
    dict = defaultdict(int)
    for instr in instructions:
        if instr[0] == "noop":
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                sum_cycles = cycle*x
                dict[cycle] = sum_cycles
        elif instr[0] == "addx":
            i = 0
            while i < 2:
                cycle += 1
                i += 1
                if cycle in [20, 60, 100, 140, 180, 220]:
                    sum_cycles = cycle*x
                    dict[cycle] = sum_cycles
            x += int(instr[1])

            if cycle in [20, 60, 100, 140, 180, 220]:
                sum_cycles = cycle*x
                dict[cycle] = sum_cycles

    print(sum(dict.values()))

# part 2 (didn't solve)
def draw_pixels(file):

    instructions = None
    with open(file) as f:
        instructions = [[x for x in line.split(' ')] for line in f.read().strip().split('\n')]

    x = 1
    cycle = 1
    pixel_range = [0, 2]
    img = [['.' for _ in range(40)] for _ in range(6)]

    row = 0
    pixel = 0
    img[row][pixel] = '#'
    pixel += 1
    for instr in instructions:
        # if cycle in range(pixel_range[0], pixel_range[1]+1):
        #     print(row, pixel)
        #     print('here1')
        #     img[row][pixel] = '#'
        #     pixel += 1
        #     if pixel == 40:
        #         pixel = 0
        #         row += 1
        if instr[0] == "noop":
            cycle += 1
            pixel_range[0], pixel_range[1] = pixel_range[0]+1, pixel_range[1]+1

            if cycle in range(pixel_range[0], pixel_range[1]+1):
                print(row, pixel)
                print('here2')
                img[row][pixel] = '#'
                pixel += 1
                if pixel == 40:
                    pixel = 0
                    row += 1

        elif instr[0] == "addx":
            i = 0
            while i < 2:
                cycle += 1

                pixel_range[0], pixel_range[1] = pixel_range[0]+1, pixel_range[1]+1

                if cycle in range(pixel_range[0], pixel_range[1]+1):
                    print(row, pixel)
                    print('here3')
                    img[row][pixel] = '#'
                    pixel+=1
                    if pixel == 40:
                        pixel = 0
                        row += 1

                i += 1
            x += int(instr[1])

            # if cycle in range(pixel_range[0], pixel_range[1]+1):
            #     print(row, pixel)
            #     print('here4')
            #     img[row][pixel] = '#'
            #     pixel += 1
            #     if pixel == 40:
            #         pixel = 0
            #         row += 1

    rows = [row for row in '\n'.join(img)]
    print(rows)
