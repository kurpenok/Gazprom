#!/usr/bin/env python3

from typing import List


def largest_number(numbers: List[str]) -> int:
    numbers.sort(reverse=True)
    return int("".join(str(number) for number in numbers))


if __name__ == "__main__":
    numbers = list(map(str, input("[>] Enter numbers: ").split()))
    print("[+] Largest number:", largest_number(numbers))
