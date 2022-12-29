#!/usr/bin/env python3

import unittest

from sprint_1.sleight_of_hand import sleight_of_hand


class SleightOfHandTestCase(unittest.TestCase):
    def test_example_1(self) -> None:
        res = sleight_of_hand(2, {1: 2, 2: 7, 3: 1})
        self.assertEqual(res, 2)

    def test_example_2(self) -> None:
        res = sleight_of_hand(4, {1: 10, 9: 6})
        self.assertEqual(res, 1)

    def test_example_3(self) -> None:
        res = sleight_of_hand(4, {1: 16})
        self.assertEqual(res, 0)
