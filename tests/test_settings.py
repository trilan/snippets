from unittest2 import TestCase
from snippets.settings import get_settings


class SettingsTests(TestCase):

    def test_get_settings(self):
        local_settings = {
            'SITE_NAME': 'My Snippets',
            'SITE_DOMAIN': 'http://example.com',
            'not_a_settings': True,
        }
        default_settings = {
            'SITE_DOMAIN': 'Code Snippets',
            'SITE_URL': '/',
        }
        self.assertEqual(get_settings(local_settings, default_settings), {
            'SITE_NAME': 'My Snippets',
            'SITE_DOMAIN': 'http://example.com',
            'SITE_URL': '/',
        })
