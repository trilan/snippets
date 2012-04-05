import os
from unittest2 import TestCase
from snippets.finder import find


TESTS_DIR = os.path.dirname(__file__)
FIXTURES_DIR = os.path.join(TESTS_DIR, 'fixtures', 'finder')


class FinderTests(TestCase):

    def test_finds_all_files_recursively(self):
        self.assertItemsEqual(find(FIXTURES_DIR), [
            os.path.join(FIXTURES_DIR, 'javascript/hello.js'),
            os.path.join(FIXTURES_DIR, 'python/hello.py'),
            os.path.join(FIXTURES_DIR, 'style.css'),
        ])
