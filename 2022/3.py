from typing import List

from utils import format_solution, puzzle_input


def func(d: List[str]) -> int:
    count = 0
    for bag in d:
        n = len(bag)
        c1, c2 = bag[: n // 2], bag[n // 2:]
        item_set = set(c1).intersection(set(c2))
        item = next(iter(item_set))
        if item.islower():
            count += ord(item) - ord("a") + 1
        else:
            count += ord(item) - ord("A") + 27

    return count


def func2(d: List[str]) -> int:
    idx = count = 0
    while idx < len(d):
        c1, c2, c3 = d[idx], d[idx + 1], d[idx + 2]
        item_set = set(c1).intersection(set(c2)).intersection(set(c3))
        item = next(iter(item_set))
        if item.islower():
            count += ord(item) - ord("a") + 1
        else:
            count += ord(item) - ord("A") + 27

        idx += 3
    return count


if __name__ == "__main__":
    data = puzzle_input(2022, 3, debug=False)
    solutions = format_solution(solver_p1=lambda: func(data), solver_p2=lambda: func2(data))
    print(solutions)
