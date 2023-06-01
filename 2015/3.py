import support.aoc_utils as aoc_utils

mapping: dict[str, tuple[int, int]] = {"^": (0, 1), "v": (0, -1), ">": (1, 0), "<": (-1, 0)}


def func1(data: str) -> int:
    x, y = 0, 0
    houses: set[tuple[int, int]] = set()
    houses.add((x, y))
    for direction in data:
        move: tuple[int, int] = mapping[direction]
        x, y = x + move[0], y + move[1]
        houses.add((x, y))
    return len(houses)


def func2(data: str) -> int:
    sx, sy = 0, 0  # santa
    rx, ry = 0, 0  # robot_santa
    houses: set[tuple[int, int]] = set()
    houses.add((sx, sy))
    for idx, direction in enumerate(data):
        move: tuple[int, int] = mapping[direction]
        if idx % 2:
            rx, ry = rx + move[0], ry + move[1]
            houses.add((rx, ry))
        else:
            sx, sy = sx + move[0], sy + move[1]
            houses.add((sx, sy))
    return len(houses)


if __name__ == "__main__":
    year, day = 2015, 3
    problem_input = aoc_utils.fetch_and_save(year=year, day=day)
    aoc_utils.submit(func1(problem_input), 1, year, day)
    aoc_utils.submit(func2(problem_input), 2, year, day)
