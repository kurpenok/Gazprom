#!/usr/bin/env python3

from typing import List as List


def generate(count: int, sequences: List[str], s="", left=0, right=0) -> List[str]:
    if left == count and right == count:
        sequences.append(s)
    else:
        if left < count:
            generate(count, sequences, s + "(", left + 1, right)
        if right < left:
            generate(count, sequences, s + ")", left, right + 1)
    return sequences


def generate_brackets_sequences(count: int) -> List[str]:
    return generate(count, [])


if __name__ == "__main__":
    count = int(input("[>] Enter count of brackets: "))
    print("[+] True brackets sequences:", generate_brackets_sequences(count))
