import collections

from .finder import find
from .snippet import Snippet
from .tag import Tag


class Repository(collections.Mapping):

    def __init__(self):
        self._snippets = {}
        self.tags = collections.defaultdict(set)

    def __getitem__(self, path):
        return self._snippets[path]

    def __iter__(self):
        return iter(self._snippets)

    def __len__(self):
        return len(self._snippets)

    def add_filepath(self, filepath):
        snippet = Snippet.from_filepath(filepath)
        self._snippets[filepath] = snippet
        for tag in snippet.metadata.tags:
            self.tags[tag].add(snippet)

    def add_repopath(self, repopath):
        for filepath in find(repopath):
            self.add_filepath(filepath)
