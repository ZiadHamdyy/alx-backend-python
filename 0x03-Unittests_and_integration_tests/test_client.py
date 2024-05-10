#!/usr/bin/env python3

"""TestGithubOrgClient"""
import unittest
import unittest.mock
from parameterized import parameterized  # type: ignore
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class that inherits from unittest.TestCase"""

    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    @unittest.mock.patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """test_org test that GithubOrgClient.org returns the correct value"""
        expected_url = f"https://api.github.com/orgs/{org_name}"
        client = GithubOrgClient(org_name)
        client.org()
        mock_get_json.assert_called_once_with(expected_url)

    @unittest.mock.patch('client.GithubOrgClient.org',
                         new_callable=unittest.mock.PropertyMock)
    def test_public_repos_url(self, mock_org):
        """test_public_repos_url"""
        mock_org.return_value = {"repos_url":
                                 "https://api.github.com/orgs/testorg/repos"}
        client = GithubOrgClient("testorg")
        self.assertEqual(client._public_repos_url,
                         "https://api.github.com/orgs/testorg/repos")

    @unittest.mock.patch('client.get_json')
    @unittest.mock.patch('client.GithubOrgClient._public_repos_url',
                         new_callable=unittest.mock.PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """test_public_repos"""
        sample_payload = [
            {"name": "repo1", "license": {"key": "MIT"}},
            {"name": "repo2", "license": {"key": "Apache"}},
            {"name": "repo3", "license": {"key": "GPL"}},
        ]

        mock_public_repos_url.return_value = \
            "https://api.github.com/orgs/testorg/repos"
        mock_get_json.return_value = sample_payload

        client = GithubOrgClient("testorg")

        repos = client.public_repos(license="MIT")

        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/testorg/repos")
        mock_public_repos_url.assert_called_once()

        self.assertEqual(repos, ["repo1"])


if __name__ == "__main__":
    unittest.main()
