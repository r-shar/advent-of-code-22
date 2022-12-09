'''
bfs
- add count of all exterior trees
- for all interior trees
    - check if curr_tree_height max( neighbors_heights )
        - add to set
- return len(set ) + count_exterior_trees
'''


def count_visible_find_scenic(file):
    visible = set()
    scenic_score = set()
    tree_grid = []

    with open(file) as f:
        for line in f:
            row = [int(height) for height in line.strip()]
            tree_grid.append(row)

    for r in range(1, len(tree_grid)-1):
        for c in range(1, len(tree_grid[0])-1):
            score = 1
            for x,y in [(0,1), (0,-1), (1,0), (-1, 0)]:
                neighbors = []
                r_, c_ = r, c
                while x + r_ >= 0 and x + r_ < len(tree_grid) and y + c_ >= 0 and y + c_ < len(tree_grid[0]):
                    r_ += x
                    c_ += y
                    neighbors.append(tree_grid[r_][c_])
                if tree_grid[r][c] > max(neighbors):
                    visible.add((r, c))
                    score *= len(neighbors)
                else:
                    # print([i+1 for i, n in enumerate(neighbors) if n >= tree_grid[r][c]])
                    score *= [i+1 for i, n in enumerate(neighbors) if n >= tree_grid[r][c]][0]
                scenic_score.add(score)

    count_exterior_trees = (2*len(tree_grid)) + (2*(len(tree_grid[0])-2))
    print(len(visible) + count_exterior_trees)
    print(max(scenic_score))
