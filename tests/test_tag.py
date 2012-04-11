from unittest2 import TestCase
from snippets.tag import Tag


class TagTests(TestCase):

    def setUp(self):
        Tag.registry.clear()

    def test_does_not_create_new_tags_with_the_same_name(self):
        self.assertIs(Tag('Django'), Tag('Django'))
        self.assertIs(Tag('Django'), Tag('django'))

    def test_first_tag_tag_name_is_saved(self):
        Tag('Django')
        self.assertEqual(Tag('django').name, 'Django')

    def test_relpath(self):
        self.assertEqual(Tag('Django').get_relpath(), 'tags/django.html')

    def test_converts_to_unicode(self):
        self.assertEqual(unicode(Tag('Django')), u'Django')
