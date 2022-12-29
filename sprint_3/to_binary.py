#!/usr/bin/env python3

def to_binary(number: int) -> int:
    result = ""
    while number > 0:
        result = str(number % 2) + result
        number = number // 2
    return int(result)


if __name__ == "__main__":
    number = int(input("[>] Enter number: "))
    print(f"[+] Binary number: {to_binary(number)}")
