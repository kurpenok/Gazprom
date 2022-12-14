#!/usr/bin/env python3

import unittest

from sprint_2.generate_brackets_sequence import generate_brackets_sequences


class NearestZeroTestCase(unittest.TestCase):
    def test_example_1(self) -> None:
        res = generate_brackets_sequences(2)
        self.assertEqual(res, ["(())", "()()"])

    def test_example_2(self) -> None:
        res = generate_brackets_sequences(3)
        self.assertEqual(res, ["((()))", "(()())", "(())()", "()(())", "()()()"])
