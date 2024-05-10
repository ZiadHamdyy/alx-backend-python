#!/usr/bin/env python3
"""TestAccessNestedMap"""

import unittest
import unittest.mock
from parameterized import parameterized  # type: ignore
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class that inherits from unittest.TestCase"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """test_access_nested_map method to test that the method returns what
        it is supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'"),
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_exception):
        """test_access_nested_map_exception. Use the assertRaises
        context manager to test that a KeyError"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_exception)


class TestGetJson(unittest.TestCase):
    """TestGetJson class that inherits from unittest.TestCase"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @unittest.mock.patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """test_get_json method to test that utils.get_json
        returns the expected result"""
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """TestMemoize class that inherits from unittest.TestCase"""

    class TestClass:
        """TestClass class that inherits from unittest.TestCase"""

        def a_method(self):
            """a_method"""
            return 42

        @memoize
        def a_property(self):
            """a_property"""
            return self.a_method()

    @unittest.mock.patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_a_method):
        """test_memoize"""
        test_instance = self.TestClass()

        result1 = test_instance.a_property
        result2 = test_instance.a_property

        mock_a_method.assert_called_once()

        self.assertEqual(result1, result2)


if __name__ == "__main__":
    unittest.main()
