class Tag(set):

    def __init__(self, name):
        self.name = name
        self.slug = name.lower()
        super(Tag, self).__init__()

    def get_relpath(self):
        return 'tags/{slug}.html'.format(slug=self.slug)
