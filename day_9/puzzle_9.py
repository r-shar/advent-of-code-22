import math
def calculate_distance(hx,hy,tx,ty):
    d = int(math.sqrt((ty-hy)**2 + (tx-hx)**2))
    return d

# part 1
def count_positions(file):
    head_moves = None
    with open(file) as f:
        head_moves = [[x for x in line.strip().split()] for line in f]

    # coordinates of head and tail
    # start at origin (head covers tail in initial state)
    hx, hy = 0, 0
    tx, ty = 0, 0

    # set to keep track of locations visited by tail
    visited = set()

    for dir, num_steps in head_moves:
        steps_to_go = int(num_steps)
        while steps_to_go > 0:
            if dir == 'R':
                hx += 1
                if calculate_distance(hx,hy,tx,ty) > 1 and ty != hy:
                    ty = hy
                    tx += 1
                elif calculate_distance(hx,hy,tx,ty) > 1:
                    tx += 1
            elif dir == 'L':
                hx -= 1
                if calculate_distance(hx,hy,tx,ty) > 1 and ty != hy:
                    ty = hy
                    tx -= 1
                elif calculate_distance(hx,hy,tx,ty) > 1:
                    tx -= 1
            elif dir == 'U':
                hy += 1
                if calculate_distance(hx,hy,tx,ty) > 1 and tx != hx:
                    tx = hx
                    ty += 1
                elif calculate_distance(hx,hy,tx,ty) > 1:
                    ty += 1
            else:
                hy -= 1
                if calculate_distance(hx,hy,tx,ty) > 1 and tx != hx:
                    tx = hx
                    ty -= 1
                elif calculate_distance(hx,hy,tx,ty) > 1:
                    ty -= 1

            visited.add((tx,ty))
            steps_to_go -= 1


    print(len(visited))
