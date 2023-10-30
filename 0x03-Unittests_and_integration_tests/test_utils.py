#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
from utils import access_nested_map

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
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """Tests `access_nested_map`'s output."""
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == '__main__':
    unittest.main()
