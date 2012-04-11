import mock
from unittest2 import TestCase

from snippets.generator import Generator
from snippets.repository import Repository
from snippets.snippet import Snippet


class GeteratorTests(TestCase):

    def setUp(self):
        self.repository = Repository()
        self.generator = Generator(self.repository, 'theme')
        self.generator._render_template = self.render_template = mock.Mock()

    def test_render_snippet(self):
        snippet = Snippet('snippets/example.py', {'date': '2012-04-01'}, ())
        result = self.generator.render_snippet(snippet)
        self.render_template.assert_called_once_with('snippet.html', {'snippet': snippet})
