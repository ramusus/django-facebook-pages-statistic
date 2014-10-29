from django.utils import timezone
from django.test import TestCase
from facebook_pages.models import Page
from facebook_pages.factories import PageFactory

from models import PageStatistic


PAGE_FANS_ID = 501842786534856


class PageStatisticTest(TestCase):

    def setUp(self):
        self.t = timezone.now()
        self.p = PageFactory(graph_id=PAGE_FANS_ID, likes_count=10, talking_about_count=20)

    def test_page_statistic_create(self):
        t = self.t
        p = self.p

        ps = PageStatistic.objects.get(id=1)
        self.assertEqual(ps.page, p)
        self.assertEqual(ps.likes_count, p.likes_count)
        self.assertEqual(ps.talking_about_count, p.talking_about_count)
        self.assertGreater(ps.updated_at, t)

    def test_test_page_statistic_update(self):
        t = timezone.now()
        p = self.p
        p.likes_count += 100
        p.talking_about_count += 100
        p.save()

        ps = PageStatistic.objects.get(id=2)
        self.assertEqual(ps.page, p)
        self.assertEqual(ps.likes_count, p.likes_count)
        self.assertEqual(ps.talking_about_count, p.talking_about_count)
        self.assertGreater(ps.updated_at, t)

    def test_null_stats_test(self):
        count = PageStatistic.objects.count()
        p = PageFactory(graph_id=123456, likes_count=None, talking_about_count=None)
        self.assertEqual(PageStatistic.objects.count(), count)
