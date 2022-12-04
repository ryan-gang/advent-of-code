from typing import List

from utils import format_solution, puzzle_input


def func(d: List[str]) -> int:
    """
    Find section intersections, whose length is equal to the smaller section.
    """
    count = 0
    for i in d:
        s1, s2 = i.split(",")
        start1, end1 = int(s1.split("-")[0]), int(s1.split("-")[1])
        start2, end2 = int(s2.split("-")[0]), int(s2.split("-")[1])
        range1 = range(start2, end2 + 1)
        range2 = range(start1, end1 + 1)
        smaller_range = min(len(range1), len(range2))
        intersection_range = range(max(start1, start2), min(end1, end2) + 1)
        if (len(intersection_range)) == smaller_range:
            count += 1

    return count


def func2(d: List[str]) -> int:
    """
    Find sections that intersect.
    """
    count = 0
    for i in d:
        s1, s2 = i.split(",")
        start1, end1 = int(s1.split("-")[0]), int(s1.split("-")[1])
        start2, end2 = int(s2.split("-")[0]), int(s2.split("-")[1])
        intersection_range = range(max(start1, start2), min(end1, end2) + 1)
        if (len(intersection_range)) > 0:
            count += 1

    return count


if __name__ == "__main__":
    data = puzzle_input(2022, 4, debug=False)
    solutions = format_solution(solver_p1=lambda: func(data), solver_p2=lambda: func2(data))
    print(solutions)
