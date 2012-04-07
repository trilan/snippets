import mock
from datetime import datetime
from pygments.formatters import HtmlFormatter
from unittest2 import TestCase
from snippets.content import Content


class ContentMetadataTests(TestCase):

    def test_has_processed_tags(self):
        def check(raw_metadata, result):
            content = Content(raw_metadata, ())
            self.assertEqual(content.metadata.tags, result)

        check({'tags': 'models, admin'}, ('models', 'admin'))
        check({}, ())

    def test_has_processed_date(self):
        def check(raw_metadata, result):
            content = Content(raw_metadata, ())
            self.assertEqual(content.metadata.date, result)

        check({'date': '2012-04-01'}, datetime(2012, 4, 1))
        check({'date': '2012-04-01 16:00'}, datetime(2012, 4, 1, 16))
        check({'date': '2012-04-01 16:00:05'}, datetime(2012, 4, 1, 16, 0, 5))


class ContentTests(TestCase):

    @mock.patch('snippets.content.Content._get_formatter')
    def test_has_formatted_source(self, get_formatter):
        content = Content({}, mock.sentinel.tokens)
        content.get_formatted_source()
        self.assertEqual(get_formatter.return_value.format.call_count, 1)
        self.assertIs(get_formatter.return_value.format.call_args[0][0], mock.sentinel.tokens)

    def test_get_formatter(self):
        content = Content({}, mock.sentinel.tokens)
        self.assertIsInstance(content._get_formatter(), HtmlFormatter)
