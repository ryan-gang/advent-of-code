import support.aoc_utils as aoc_utils
import hashlib


def func(key: str, magic_number: int) -> int:
    i, flag = -1, False
    while not flag:
        i += 1
        plaintext = f"{key}{i}".encode()
        hash = hashlib.md5(plaintext).hexdigest()
        flag = hash.startswith("0" * magic_number)
    return i


if __name__ == "__main__":
    year, day = 2015, 4
    problem_input = aoc_utils.fetch_and_save(year=year, day=day)
    aoc_utils.submit(func(problem_input, magic_number=5), 1, year, day)
    aoc_utils.submit(func(problem_input, magic_number=6), 2, year, day)
