import codecs
import errno
import os
from jinja2 import Environment, FileSystemLoader
from .paginator import Paginator


class Generator(object):

    def __init__(self, repository, theme):
        self.repository = repository
        self.template_environment = Environment(loader=FileSystemLoader(theme))

    def _render_template(self, name, context):
        template = self.template_environment.get_template(name)
        return template.render(context)

    def render_index(self, page):
        return self._render_template('index.html', {'page': page})

    def render_snippet(self, snippet):
        tags = []
        for tagname in snippet.metadata.tags:
            tags.append(self.repository.tags[tagname.lower()])
        return self._render_template('snippet.html', {'snippet': snippet, 'tags': tags})

    def render_tag(self, tag):
        snippets = list(tag)
        snippets.sort(key=lambda s: s.metadata.date, reverse=True)
        return self._render_template('tag.html', {'tag': tag, 'snippets': snippets})

    def write(self, filepath, content):
        try:
            os.makedirs(os.path.dirname(filepath))
        except OSError, e:
            if e.errno != errno.EEXIST:
                raise
        with codecs.open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    def generate(self, output):
        snippets = self.repository.values()
        snippets.sort(key=lambda s: s.metadata.date, reverse=True)

        for page in Paginator(snippets):
            filepath = os.path.join(output, page.get_relpath())
            self.write(filepath, self.render_index(page))

        for snippet in snippets:
            filepath = os.path.join(output, snippet.get_relpath())
            self.write(filepath, self.render_snippet(snippet))

        for tag in self.repository.tags.values():
            filepath = os.path.join(output, tag.get_relpath())
            self.write(filepath, self.render_tag(tag))
