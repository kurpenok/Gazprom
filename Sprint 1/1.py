#!/usr/bin/env python

from typing import List


def nearest_zero(plots: List[int]) -> str:
    len_array = len(plots)
    distance_to_zero = [0] * len_array

    last_zero = -len_array

    for i in range(len_array):
        if plots[i]:
            distance_to_zero[i] = i - last_zero
        else:
            last_zero = i

    last_zero = 2 * len_array

    for i in reversed(range(len_array)):
        if plots[i]:
            distance_to_zero[i] = min(last_zero - i, distance_to_zero[i])
        else:
            last_zero = i

    return " ".join(str(distance) for distance in distance_to_zero)


if __name__ == "__main__":
    plots = list(map(int, input("[>] Enter plots: ").split()))
    print("[+] Nearest zero:", nearest_zero(plots))
