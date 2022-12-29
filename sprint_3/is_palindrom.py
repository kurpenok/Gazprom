#!/usr/bin/env python3

import re


def is_palindrom(s: str) -> bool:
    s = re.compile("[^a-z]").sub("", s.lower())
    return s == s[::-1]


if __name__ == "__main__":
    s = input("[>] Enter string: ")
    print("[+] Is palidrom:", is_palindrom(s))
