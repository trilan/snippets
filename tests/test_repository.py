import mock
from unittest2 import TestCase
from snippets.repository import Repository


class RepositoryTests(TestCase):

    def setUp(self):
        self.repository = Repository()

    @mock.patch('snippets.snippet.Snippet.from_filepath')
    def test_adds_filepaths(self, from_filepath):
        self.repository.add_filepath('snippets/example.py')
        from_filepath.assert_called_once_with('snippets/example.py')
        self.assertIs(self.repository['snippets/example.py'], from_filepath.return_value)

    @mock.patch('snippets.repository.find')
    @mock.patch('snippets.repository.Repository.add_filepath')
    def test_adds_repopaths(self, add_filepath, find):
        find.return_value = ('snippets/example.py', 'snippets/example.js')
        self.repository.add_repopath('snippets')
        find.assert_called_once_with('snippets')
        self.assertEqual(add_filepath.mock_calls, [
            mock.call('snippets/example.py'),
            mock.call('snippets/example.js'),
        ])
