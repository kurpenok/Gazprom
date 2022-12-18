#!/usr/bin/env python3

from typing import List


def largest_number(count: int, numbers: List[str]) -> int:
    assert count != len(numbers), "[-] The lengths of the lists do not match!"

    numbers.sort(reverse=True)
    return int("".join(str(number) for number in numbers))


if __name__ == "__main__":
    count = int(input("[>] Enter count of numbers: "))
    numbers = list(map(str, input("[>] Enter numbers: ").split()))
    print("[+] Largest number:", largest_number(count, numbers))
