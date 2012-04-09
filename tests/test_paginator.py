from unittest2 import TestCase
from snippets.paginator import Paginator


class PaginatorTests(TestCase):

    def setUp(self):
        self.paginator = Paginator(range(60))

    def test_len(self):
        self.assertEqual(len(Paginator(range(0))), 1)
        self.assertEqual(len(Paginator(range(1))), 1)
        self.assertEqual(len(Paginator(range(20))), 1)
        self.assertEqual(len(Paginator(range(21))), 2)

    def test_page_has_prev(self):
        self.assertFalse(self.paginator.get_page(1).has_prev)
        self.assertTrue(self.paginator.get_page(2).has_prev)
        self.assertTrue(self.paginator.get_page(3).has_prev)

    def test_page_has_next(self):
        self.assertTrue(self.paginator.get_page(1).has_next)
        self.assertTrue(self.paginator.get_page(2).has_next)
        self.assertFalse(self.paginator.get_page(3).has_next)

    def test_page_has_next(self):
        self.assertEqual(self.paginator.get_page(1).get_relpath(), 'index.html')
        self.assertEqual(self.paginator.get_page(2).get_relpath(), 'page-2.html')
        self.assertEqual(self.paginator.get_page(3).get_relpath(), 'page-3.html')
