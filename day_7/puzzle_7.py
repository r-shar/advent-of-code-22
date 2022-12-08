from collections import defaultdict
from os import path, sep


def calculate_total_sizes(file):
    p1 = 0
    p2 = float("inf")
    cwd = ""
    size_dict = defaultdict(int)

    with open(file) as f:
        for line in f:
            l = line.strip().split(" ")

            if l[0] == "$" and l[1] == "cd":
                cwd = path.normpath(path.join(cwd, l[2]))

            if l[0].isnumeric():
                directories = cwd.split(sep)

                for i in range(len(directories)):
                    dir_path = path.normpath(path.join(*directories[: i + 1]))
                    size_dict[dir_path] += int(l[0])

    available = 7e7 - size_dict["."]
    sizes = size_dict.values()

    p1 = sum((v for v in sizes if v <= 1e5))
    p2 = min((v for v in sizes if v + available >= 3e7))

    print("part1:", p1, "part2:",p2)
