import collections

from .finder import find
from .snippet import Snippet


class Repository(collections.Mapping):

    def __init__(self):
        self._snippets = {}

    def __getitem__(self, path):
        return self._snippets[path]

    def __iter__(self):
        return iter(self._snippets)

    def __len__(self):
        return len(self._snippets)

    def add_filepath(self, filepath):
        self._snippets[filepath] = Snippet.from_filepath(filepath)

    def add_repopath(self, repopath):
        for filepath in find(repopath):
            self.add_filepath(filepath)
