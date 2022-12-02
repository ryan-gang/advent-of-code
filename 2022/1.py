from heapq import nlargest
from typing import List

from utils import format_solution, puzzle_input


def calorie_counting_1(calories: List[str]) -> int:
    """Running count, keep a track of max count."""
    calorie, max_calories = 0, 0
    for c in calories:
        if c == "":
            max_calories = max(max_calories, calorie)
            calorie = 0
        else:
            calorie += int(c)
    max_calories = max(max_calories, calorie)
    return max_calories


def calorie_counting_2(calories: List[str]) -> int:
    """Push running counts, into heap, return nlargest."""
    calorie = 0
    heap = []
    for c in calories:
        if c == "":
            heap.append(calorie)
            calorie = 0
        else:
            calorie += int(c)
    heap.append(calorie)
    return sum(nlargest(3, heap))


if __name__ == "__main__":
    data = puzzle_input(2022, 1, debug=False)
    solutions = format_solution(
        solver_p1=lambda: calorie_counting_1(data),
        solver_p2=lambda: calorie_counting_2(data),
    )
    print(solutions)
