import support.aoc_utils as aoc_utils


def func1(input_data: str) -> int:
    paper = 0
    data = input_data.split("\n")
    for dimensions in data:
        l, w, h = map(int, dimensions.split("x"))
        paper += (2 * (l * w + w * h + h * l)) + min(l * w, w * h, h * l)
    return paper


def func2(input_data: str) -> int:
    ribbon = 0
    data = input_data.split("\n")
    for dimensions in data:
        l, w, h = map(int, dimensions.split("x"))
        ribbon += 2 * min(l + w, w + h, h + l)
        ribbon += l * w * h
    return ribbon


if __name__ == "__main__":
    year, day = 2015, 2
    problem_input = aoc_utils.fetch_and_save(year=year, day=day)
    print(func1(problem_input))
    print(func2(problem_input))
    # aoc_utils.submit(func1(problem_input), 1, year, day)
    # aoc_utils.submit(func2(problem_input), 2, year, day)
