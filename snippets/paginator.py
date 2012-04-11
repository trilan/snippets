from math import ceil


class Paginator(object):

    def __init__(self, snippets, per_page=20):
        self.snippets = snippets
        self.per_page = per_page

    def __len__(self):
        return int(ceil(len(self.snippets) / float(self.per_page))) or 1

    def __iter__(self):
        for number0 in range(len(self)):
            yield self.get_page(number0 + 1)

    def get_page(self, number):
        start = self.per_page * (number - 1)
        end = start + self.per_page
        return Page(self.snippets[start:end], number, self)


class Page(object):

    def __init__(self, snippets, number, paginator):
        self.snippets = snippets
        self.number = number
        self.paginator = paginator

    @property
    def has_prev(self):
        return self.number > 1

    @property
    def has_next(self):
        return self.number < len(self.paginator)

    def get_relpath(self):
        if self.number == 1:
            return 'index.html'
        return 'page-{number}.html'.format(number=self.number)
