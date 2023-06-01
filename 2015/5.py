from typing import Generator
import support.aoc_utils as aoc_utils
from collections import Counter

VOWELS = set("aeiou")
RESTRICTED = set(["ab", "cd", "pq", "xy"])


def generate_consecutive_substrings(string: str, length: int) -> Generator[str, None, None]:
    # Type hints are : Generator[yield_type, send_type, return_type]
    for i in range(len(string) - (length - 1)):
        yield string[i : i + length]


def check_consecutive_letters(string: str) -> bool:
    flag = False
    substrings = generate_consecutive_substrings(string, length=2)
    for substring in substrings:
        flag = len(set(substring)) == 1
        if flag:
            break
    return flag


def check_prohibited_substrings(string: str) -> bool:
    substrings = generate_consecutive_substrings(string, length=2)
    flag = True
    for substring in substrings:
        if substring in RESTRICTED:
            flag = False
            break
    return flag


def check_vowel_count(string: str, required_count: int) -> bool:
    return len(list(filter(lambda x: x in VOWELS, string))) >= required_count


def func1(input_data: str) -> int:
    count = 0
    data = input_data.split("\n")
    for string in data:
        count += (
            check_vowel_count(string, required_count=3)
            and check_consecutive_letters(string)
            and check_prohibited_substrings(string)
        )
    return count


def check_letter_inbetween_substring(string: str) -> bool:
    flag = False
    substrings = generate_consecutive_substrings(string, length=3)
    for substring in substrings:
        a, _, c = substring
        if a == c:
            flag = True
            break
    return flag


def check_repeating_substring(string: str) -> bool:
    d: dict[str, int] = Counter()
    substrings = generate_consecutive_substrings(string, length=2)
    prev = ""
    for substring in substrings:
        if (substring in d and prev != substring) or d[substring] >= 2:
            return True
        else:
            prev = substring
            d[substring] += 1
    return False


def func2(input_data: str) -> int:
    count = 0
    data = input_data.split("\n")
    for string in data:
        count += check_letter_inbetween_substring(string) and check_repeating_substring(string)
    return count


if __name__ == "__main__":
    year, day = 2015, 5
    problem_input = aoc_utils.fetch_and_save(year=year, day=day)
    aoc_utils.submit(func1(problem_input), 1, year, day)
    aoc_utils.submit(func2(problem_input), 2, year, day)
