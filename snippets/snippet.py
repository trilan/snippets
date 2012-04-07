from datetime import datetime

from pygments import format
from pygments.formatters import HtmlFormatter


DATE_FORMATS = (
    '%Y-%m-%d',
    '%Y-%m-%d %H:%M',
    '%Y-%m-%d %H:%M:%S',
)


class SnippetMetadata(object):

    def __init__(self, raw_metadata):
        self.raw_metadata = raw_metadata

    @property
    def tags(self):
        tags = self.raw_metadata.get('tags', '').strip()
        if not tags:
            return ()
        return tuple(tag.strip() for tag in tags.split(','))

    @property
    def date(self):
        raw_date = self.raw_metadata.get('date')
        if not raw_date:
            raise ValueError('raw date is not set')
        for date_format in DATE_FORMATS:
            try:
                return datetime.strptime(raw_date, date_format)
            except ValueError:
                pass
        raise ValueError('raw date format urecognized')

    def __getattr__(self, name):
        try:
            return self.raw_metadata[name]
        except KeyError:
            raise AttributeError


class Snippet(object):

    def __init__(self, raw_metadata, tokens):
        self.metadata = SnippetMetadata(raw_metadata)
        self.tokens = tokens

    def _get_formatter(self):
        return HtmlFormatter()

    def get_formatted_source(self):
        return format(self.tokens, self._get_formatter())
