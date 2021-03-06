import codecs
import errno
import os
import shutil
from jinja2 import Environment, FileSystemLoader
from .paginator import Paginator


class Generator(object):

    def __init__(self, repository, theme, extra_context=None):
        self.repository = repository
        self.theme = theme
        self.extra_context = extra_context or {}
        self.template_environment = Environment(
            loader=FileSystemLoader(os.path.join(theme, 'templates')),
        )

    def _render_template(self, name, context):
        template = self.template_environment.get_template(name)
        template_context = self.extra_context.copy()
        template_context.update(context)
        return template.render(template_context)

    def render_index(self, page):
        return self._render_template('index.html', {'page': page})

    def render_snippet(self, snippet):
        return self._render_template('snippet.html', {'snippet': snippet})

    def render_tag(self, tag, snippets):
        snippets = list(snippets)
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

    def copy_static(self, output):
        source = os.path.join(self.theme, 'static')
        target = os.path.join(output, 'static')
        if os.path.isdir(source):
            if os.path.exists(target):
                shutil.rmtree(target)
            shutil.copytree(source, target)

    def generate(self, output):
        snippets = self.repository.values()
        snippets.sort(key=lambda s: s.metadata.date, reverse=True)

        self.copy_static(output)

        for page in Paginator(snippets):
            filepath = os.path.join(output, page.get_relpath())
            self.write(filepath, self.render_index(page))

        for snippet in snippets:
            filepath = os.path.join(output, snippet.get_relpath())
            self.write(filepath, self.render_snippet(snippet))

        for tag, tag_snippets in self.repository.tags.items():
            filepath = os.path.join(output, tag.get_relpath())
            self.write(filepath, self.render_tag(tag, tag_snippets))
