from pygments.token import Comment, Text
from unittest2 import TestCase
from snippets.metadata_parser import parse_metadata


class MetadataParserTests(TestCase):

    def test_parses_single_line_comments_with_metadata(self):
        metadata, comments = parse_metadata((
            (Comment, u'# !title: Django and SQLAlchemy'), (Text, u'\n'),
            (Comment, u'# !date: 2012-04-01 12:00'), (Text, u'\n'),
        ))
        self.assertEqual(metadata['title'], 'Django and SQLAlchemy')
        self.assertEqual(metadata['date'], '2012-04-01 12:00')

        metadata, comments = parse_metadata((
            (Comment.Single, u'// !title: Paginated Collections'),
        ))
        self.assertEqual(metadata['title'], 'Paginated Collections')

    def test_parses_multi_line_comments_with_metadata(self):
        comment = (
            u'/*\n'
            u' *  !title: Simple Backbone.js App Structure\n'
            u' *  !tags: backbone, javascript\n'
            u' */'
        )
        metadata, comments = parse_metadata((
            (Comment, comment), (Text, u'\n'),
        ))
        self.assertEqual(metadata['title'], 'Simple Backbone.js App Structure')
        self.assertEqual(metadata['tags'], 'backbone, javascript')

        metadata, comments = parse_metadata(((Comment.Multiline, comment),))
        self.assertEqual(metadata['title'], 'Simple Backbone.js App Structure')
        self.assertEqual(metadata['tags'], 'backbone, javascript')

    def test_skips_comments_without_metadata(self):
        metadata, comments = parse_metadata((
            (Comment, u'# !title: Django and SQLAlchemy'), (Text, u'\n'),
            (Comment, u'# Just a code comment'), (Text, u'\n'), (Text, u'\n'),
            (Comment, u'# !date: 2012-04-01'), (Text, u'\n'), (Text, u'\n'),
        ))
        self.assertEqual(tuple(comments), (
            (Comment, u'# Just a code comment'), (Text, u'\n'), (Text, u'\n'),
        ))
