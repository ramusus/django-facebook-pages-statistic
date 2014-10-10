
from django.test import TestCase

from fbparse import likes_shares_parse


class ParseTest(TestCase):
    def test_likes_shares_parse(self):
        d = likes_shares_parse('samsung')
        self.assertIsInstance(d, dict)
        self.assertIn("likes", d)
        self.assertIn("shares", d)
        self.assertIsInstance(d["likes"], int)
        self.assertIsInstance(d["shares"], int)

