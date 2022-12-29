#!/usr/bin/env python3

import unittest

from sprint_3.is_palindrom import is_palindrom


class IsPalindromTest(unittest.TestCase):
    def test_case_1(self) -> None:
        result = is_palindrom("A man, a plan, a canal: Panama")
        self.assertEqual(result, True)

    def test_case_2(self) -> None:
        result = is_palindrom("zo")
        self.assertEqual(result, False)
