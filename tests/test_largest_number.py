#!/usr/bin/env python3

import unittest

from sprint_2.largest_number import largest_number


class NearestZeroTestCase(unittest.TestCase):
    def test_example_1(self) -> None:
        res = largest_number(["1", "783", "2"])
        self.assertEqual(res, 78321)

    def test_example_2(self) -> None:
        res = largest_number(["2", "4", "5", "2", "10"])
        self.assertEqual(res, 542210)
