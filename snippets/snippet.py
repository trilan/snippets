import os
from datetime import datetime

from pygments import format
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_for_filename

from .metadata_parser import parse_metadata
from .tag import Tag
from .token_splitter import split
from .utils import read


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
        return tuple(Tag(tag.strip()) for tag in tags.split(','))

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

    def __init__(self, filepath, raw_metadata, tokens):
        self.filepath = filepath
        self.filename = os.path.basename(filepath)
        self.metadata = SnippetMetadata(raw_metadata)
        self.tokens = tokens

    @classmethod
    def from_source(cls, filepath, source):
        lexer = get_lexer_for_filename(filepath)
        tokens = lexer.get_tokens(source)
        comments, tokens = split(tokens)
        raw_metadata, comments = parse_metadata(comments)
        return cls(filepath, raw_metadata, tuple(comments) + tuple(tokens))

    @classmethod
    def from_filepath(cls, filepath):
        return cls.from_source(filepath, read(filepath))

    def _get_formatter(self):
        return HtmlFormatter()

    def get_relpath(self):
        return '{date:%Y}/{date:%m}/{slug}.html'.format(
            date=self.metadata.date,
            slug=getattr(self.metadata, 'slug', self.filename),
        )

    def get_formatted_source(self):
        return format(self.tokens, self._get_formatter())
