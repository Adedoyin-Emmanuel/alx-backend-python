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
        ({}, ("a",), "Key not found: 'a' in {}"),
        ({"a": 1}, ("a", "b"), "Key not found: 'b' in {'a': 1}"),
    ])
    def test_access_nested_map_exception(self, nested_map,
                                         path, expected_exception_message):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        actual_exception_message = str(context.exception)
        self.assertEqual(actual_exception_message, expected_exception_message)


if __name__ == '__main__':
    unittest.main()
