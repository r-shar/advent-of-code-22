#part 2

from collections import deque, defaultdict
import string

def get_neighbors(r, c, grid):
    neighbors = []
    for x, y in [(0,1),(1,0),(-1,0),(0,-1)]:
        if r+x >= 0 and r+x < len(grid) and c+y >= 0 and c+y < len(grid[0]):

            player_height = grid[r][c]
            visit_height = grid[r+x][c+y]
            all_heights = 'S' + string.ascii_lowercase + 'E'
            height_diff = all_heights.find(player_height) - all_heights.find(visit_height)

            if height_diff <= 1:
                neighbors.append((r+x, c+y))

    return neighbors

def find_fewest_steps(file):
    grid = []
    s, e_positions = None, []
    with open(file) as f:
        for l in f:
            row = [x for x in l.strip()]
            grid.append(row)

    # find s and e
    # initialize distances
    distances = defaultdict(int)
    max_dist = float("inf")

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            distances[(r,c)] = max_dist
            if grid[r][c] in ['S', 'a']:
                e_positions.append((r,c))
            if grid[r][c] == 'E':
                s = (r, c)
                distances[(r,c)] = 0

    q = deque([s])
    visited = set()

    while q:
        item = q.popleft()
        visited.add(item)

        neighbors = get_neighbors(item[0], item[1], grid)

        for neighbor in neighbors:
            # update neighbor's distance
            distances[neighbor] = min(distances[neighbor], distances[item] + 1)

            if neighbor in e_positions:
                return distances[neighbor]

            if neighbor not in visited and neighbor not in q:
                q.append(neighbor)

    return -1

print(find_fewest_steps("input_12.txt"))
