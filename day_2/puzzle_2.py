'''
input: file of strings
output: int

first letter = opponent's move
second letter = your move

score = sum(your move, outcome of round)
    X = 1 (rock)
    Y = 2 (paper)
    Z = 3 (scissors)

    LOST = 0
    DRAW = 3
    WIN = 6

winning combinations:
CX, BZ, AY
'''
# part 1 (assuming gameplay follows guide)
def calculate_total_score(file):
    sum_moves = 0
    sum_outcomes = 0

    move_mapping = {"X": "A", "Y":"B", "Z":"C"}
    moves = {"X": 1, "Y":2, "Z":3}
    winning_outcomes = {"CX", "BZ", "AY"}

    try:
        f = open(file)
        for line in f:
            l = (line.strip()).replace(" ", "")
            sum_moves += int(moves[l[1]])
            if l in winning_outcomes:
                sum_outcomes += 6
            elif move_mapping[l[1]] == l[0]:
                sum_outcomes += 3
    finally:
        f.close()

    return sum_moves + sum_outcomes

'''
second column = what the outcome needs to be :
    X = lose
    Y = draw
    Z = win

'''
# part 2
def calculate_score_2(file):
    sum_moves = 0
    sum_outcomes = 0

    you_lose = {"A":"C", "B":"A", "C":"B"}
    you_win = {"A":"B", "B":"C", "C":"A"}
    points = {"A":1, "B":2, "C":3}
    outcome_points = {"X": 0, "Y": 3, "Z": 6}

    try:
        f = open(file)
        for line in f:
            l = (line.strip()).replace(" ", "")
            # based on needed outcome for round,
            # determine move, and add points
            sum_outcomes += outcome_points[l[1]]
            if l[1] == "X":
                move_to_lose = you_lose[l[0]]
                sum_moves += points[move_to_lose]
            elif l[1] == "Y":
                sum_moves += points[l[0]]
            else:
                move_to_win = you_win[l[0]]
                sum_moves += points[move_to_win]
    finally:
        f.close()

    return sum_moves + sum_outcomes
def main():
    print(calculate_total_score("/Users/rashmisharma/Desktop/advent_of_code_22/day_2/test_2.txt"))
    print(calculate_total_score("/Users/rashmisharma/Desktop/advent_of_code_22/day_2/input_2.txt"))
    print(calculate_score_2("/Users/rashmisharma/Desktop/advent_of_code_22/day_2/test_2.txt"))
    print(calculate_score_2("/Users/rashmisharma/Desktop/advent_of_code_22/day_2/input_2.txt"))
main()
