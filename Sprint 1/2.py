#!/usr/bin/env python3

from typing import Dict


def sleight_of_hand(k: int, digits: Dict[int, int]) -> int:
    score = 0

    for count in digits.values():
        if count <= 2 * k:
            score += 1

    return score


if __name__ == "__main__":
    k = int(input("[>] Enter count of clicks: "))

    digits = {}
    for i in range(4):
        data = input(f"[>] Enter {i + 1} row: ")
        for digit in data:
            if digit.isdigit():
                digits[digit] = digits.get(digit, 0) + 1

    print("[+] Maximum possible number of points:", sleight_of_hand(k, digits))
