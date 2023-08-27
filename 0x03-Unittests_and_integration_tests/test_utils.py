#!/usr/bin/env python3
"""Parameterized units"""
import unittest
import requests
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any
from parameterized import parameterized

class TestAccessNestedMap(unittest.TestCase):
    """Class unittest for accessing Nested Map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: int) -> None:
        """
        Test nested map to access the value of nested_map
        using the path(Any)
        """
        self.assertEqual(access_nested_map(nested_map, path),
                         expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """Test nested map exception"""
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test GetJson class"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test for get json method"""
        mock_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Test the memoization decorator, memoize"""
    class TestClass:
        """Test that utils.memoize decorator works as intended"""
        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    with patch.object(TestClass, 'a_method') as mock_a_method:
            instance = TestClass()
            instance.a_property()
            instance.a_property()
            mock_a_method.assert_called_once()
