import os

from pygments.lexers import get_lexer_for_filename
from pygments.token import Comment, Text, Keyword, String, Operator, Punctuation, Number

from snippets.token_splitter import split
from unittest2 import TestCase


TESTS_DIR = os.path.dirname(__file__)
FIXTURES_DIR = os.path.join(TESTS_DIR, 'fixtures', 'token_splitter')


class TokenSplitterTests(TestCase):

    def get_tokens(self, fixture):
        with open(os.path.join(FIXTURES_DIR, fixture)) as f:
            source = f.read()
        lexer = get_lexer_for_filename(fixture)
        return lexer.get_tokens(source)

    def test_handles_single_line_comments(self):
        comments, source = split(self.get_tokens('python.py'))
        self.assertEqual(tuple(comments), (
            (Comment, u'# This is a header comment'), (Text, u'\n'),
            (Comment, u'# splitted into two lines.'), (Text, u'\n'),
            (Text, u'\n'), (Comment, u'# Hello!'), (Text, u'\n'),
        ))
        self.assertEqual(tuple(source), (
            (Keyword, u'print'), (Text, u' '), (String, u"'"),
            (String, u'Hello, World!'), (String, u"'"), (Text, u'\n'),
        ))

        comments, source = split(((Comment.Single, u'// comment'),))
        self.assertEqual(tuple(comments), ((Comment.Single, u'// comment'),))
        self.assertEqual(tuple(source), ())

    def test_handles_multi_line_comments(self):
        comments, source = split(self.get_tokens('style.css'))
        self.assertEqual(tuple(comments), (
            (Comment, u'/*\n * !tags: base\n */'), (Text, u'\n\n'),
        ))
        self.assertEqual(tuple(source), (
            (Operator, u'*'), (Text, u' '), (Punctuation, u'{'),
            (Text, u'\n  '), (Keyword, u'padding'), (Operator, u':'),
            (Text, u' '), (Number, u'0'), (Punctuation, u';'),
            (Text, u'\n  '), (Keyword, u'margin'), (Operator, u':'),
            (Text, u' '), (Number, u'0'), (Punctuation, u';'), (Text, u'\n'),
            (Punctuation, u'}'), (Text, u'\n'),
        ))

        comments, source = split(((Comment.Multiline, u'/* */'),))
        self.assertEqual(tuple(comments), ((Comment.Multiline, u'/* */'),))
        self.assertEqual(tuple(source), ())

    def test_handles_empty_text_tokens(self):
        comments, source = split(((Text, u''), (Comment, u'// comment')))
        self.assertEqual(tuple(comments), ((Text, u''), (Comment, u'// comment')))
        self.assertEqual(tuple(source), ())
