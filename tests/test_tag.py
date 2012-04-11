import mock
from unittest2 import TestCase
from snippets.tag import Tag


class TagTests(TestCase):

    def setUp(self):
        Tag.registry.clear()

    def test_does_not_create_new_tags_with_the_same_name(self):
        self.assertIs(Tag('Django'), Tag('Django'))
        self.assertIs(Tag('Django'), Tag('django'))

    def test_saves_snippets_between_objects(self):
        tag = Tag('Django')
        tag.add(mock.sentinel.snippet1)
        tag.add(mock.sentinel.snippet2)
        self.assertItemsEqual(Tag('django'), [mock.sentinel.snippet1, mock.sentinel.snippet2])

    def test_relpath(self):
        self.assertEqual(Tag('Django').get_relpath(), 'tags/django.html')

    def test_converts_to_unicode(self):
        self.assertEqual(unicode(Tag('Django')), u'Django')
