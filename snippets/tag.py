class Tag(set):
    """Represents a snippets tag. Tags with the same slug are the same objects.
    So, e.g., tags with names ``Django``, ``django`` and ``DJANGO`` will share
    the same set of snippets.
    """

    registry = {}

    def __new__(cls, name):
        slug = name.lower()
        if slug in cls.registry:
            return cls.registry[slug]
        return super(Tag, cls).__new__(cls, name)

    def __init__(self, name):
        slug = name.lower()
        if slug not in self.registry:
            self.name = name
            self.slug = slug
            super(Tag, self).__init__()
            self.registry[slug] = self

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return u'<Tag %s>' % self.name

    def get_relpath(self):
        return 'tags/{slug}.html'.format(slug=self.slug)
