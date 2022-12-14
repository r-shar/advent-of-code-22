from collections import deque, defaultdict
import string

def get_neighbors(r, c, grid):
    neighbors = []
    for x, y in [(0,1),(1,0),(-1,0),(0,-1)]:
        if r+x >= 0 and r+x < len(grid) and c+y >= 0 and c+y < len(grid[0]):

            player_height = grid[r][c]
            visit_height = grid[r+x][c+y]
            all_heights = 'S' + string.ascii_lowercase + 'E'
            height_diff = all_heights.find(visit_height) - all_heights.find(player_height)

            if height_diff <= 1:
                neighbors.append((r+x, c+y))

    return neighbors

def find_fewest_steps(file):
    grid = []
    s, e = None, None
    with open(file) as f:
        for l in f:
            row = [x for x in l.strip()]
            grid.append(row)

    # find s and e
    # initialize distances
    distances = defaultdict(int)
    max_dist = float("inf")

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'S':
                s = (r, c)
                distances[(r,c)] = 0
            elif grid[r][c] == 'E':
                e = (r, c)
            else:
                distances[(r,c)] = max_dist


    q = deque([s])
    visited = set()

    while q:
        item = q.popleft()
        visited.add(item)

        neighbors = get_neighbors(item[0], item[1], grid)

        if e in neighbors:
            print(distances[item] + 1)
            break

        for neighbor in neighbors:
            # update neighbor's distance
            distances[neighbor] = min(distances[neighbor], distances[item] + 1)

            if neighbor not in visited and neighbor not in q:
                q.append(neighbor)



find_fewest_steps("input_12.txt")
