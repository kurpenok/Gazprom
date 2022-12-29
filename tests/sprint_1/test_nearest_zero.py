#!/usr/bin/env python3

import unittest

from sprint_1.nearest_zero import nearest_zero


class NearestZeroTestCase(unittest.TestCase):
    def test_example_1(self) -> None:
        res = nearest_zero([0, 1, 4, 9, 0])
        self.assertEqual(res, [0, 1, 2, 1, 0])

    def test_example_2(self) -> None:
        res = nearest_zero([0, 7, 9, 4, 8, 20])
        self.assertEqual(res, [0, 1, 2, 3, 4, 5])
