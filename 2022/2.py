from typing import List

from utils import format_solution, puzzle_input


def compare(entity1: str, entity2: str) -> int:
    """
    Returns result from the pov of entity1, 6 if won, 0 if lost, 3 for draw.
    """
    actions = {
        "rock": {"scissors": 6, "paper": 0},
        "paper": {"scissors": 0, "rock": 6},
        "scissors": {"rock": 0, "paper": 6},
    }
    if entity1 == entity2:
        return 3
    return actions[entity1][entity2]


def predict(entity2: str, output: str) -> str:
    """
    Given entity2 and output, return entity1 as a str.
    Actions are from the pov of entity1, so we reverse the output.
    (Reversed the action_mapping.)
    """
    action_mapping = {"X": 6, "Y": 3, "Z": 0}
    actions = {
        "rock": {"scissors": 6, "paper": 0},
        "paper": {"scissors": 0, "rock": 6},
        "scissors": {"rock": 0, "paper": 6},
    }
    if action_mapping[output] == 3:  # Draw
        return entity2
    for entity1 in actions[entity2]:
        if actions[entity2][entity1] == action_mapping[output]:
            break
    return entity1


def func(d: List[str]) -> int:
    mapping = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors",
    }
    point_mapping = {"rock": 1, "paper": 2, "scissors": 3}
    points = 0
    for i in d:
        their, mine = i.split(" ")
        their, mine = mapping[their], mapping[mine]
        p = compare(mine, their)
        points += p + point_mapping[mine]

    return points


def func2(d: List[str]) -> int:
    mapping = {"A": "rock", "B": "paper", "C": "scissors"}
    point_mapping = {"rock": 1, "paper": 2, "scissors": 3}
    result_mapping = {"X": 0, "Y": 3, "Z": 6}
    points = 0
    for i in d:
        their, result = mapping[i.split(" ")[0]], i.split(" ")[1]
        mine = predict(their, result)
        points += result_mapping[result] + point_mapping[mine]

    return points


if __name__ == "__main__":
    data = puzzle_input(2022, 2, debug=False)
    solutions = format_solution(solver_p1=lambda: func(data), solver_p2=lambda: func2(data))
    print(solutions)
