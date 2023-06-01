import support.aoc_utils as aoc_utils

mapping = {"(": 1, ")": -1}


def func1(data: str) -> int:
    floor = 0
    for char in data:
        floor += mapping[char]
    return floor


def func2(data: list[str]) -> int:
    floor = idx = 0
    for idx, char in enumerate(data):
        floor += mapping[char]
        if floor < 0:
            break
    return idx + 1


if __name__ == "__main__":
    year, day = 2015, 1
    problem_input = aoc_utils.fetch_and_save(year=year, day=day)
    aoc_utils.submit(func1(problem_input), 1, year, day)
