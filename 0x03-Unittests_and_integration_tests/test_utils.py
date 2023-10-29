#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map  # Import the function to be tested

"""Create a test class that inherits from unittest.TestCase"""


class TestAccessNestedMap(unittest.TestCase):
    """Using the @parameterized.expand decorator
    to define multiple test cases
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
