#!/usr/bin/env python3

import unittest

from sprint_3.to_binary import to_binary


class ToBinary(unittest.TestCase):
    def test_case_1(self) -> None:
        result = to_binary(5)
        self.assertEqual(result, 101)
    
    def test_case_w(self) -> None:
        result = to_binary(14)
        self.assertEqual(result, 1110)
