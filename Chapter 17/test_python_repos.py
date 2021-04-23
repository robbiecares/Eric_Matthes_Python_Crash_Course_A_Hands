import unittest
from python_repos import make_call


class StatusCodeTestCase(unittest.TestCase):
    """Tests for 'hn_submissions.py' """

    def test_status_code(self):
        """test to confirm that the API call was successful"""
        r, status = make_call('https://api.github.com/search/repositories?q=language:python&sort=stars',headers={'Accept': 'application/vnd.github.v3+json'})
        self.assertEqual(status,200)
        response_dict = r.json()
        total_count = int(response_dict['total_count'])
        self.assertGreaterEqual(total_count,1_000_000)
        total_repo_dicts = len(response_dict['items'])
        self.assertEqual(total_repo_dicts,30)

if __name__ == "__main__":
    unittest.main()
