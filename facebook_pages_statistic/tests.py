from django.utils import timezone
from django.test import TestCase
from facebook_pages.models import Page
from facebook_pages.factories import PageFactory
from models import PageStatistic
from datetime import datetime

PAGE_FANS_ID = 19292868552


class FacebookPageStatisticTest(TestCase):

    def test_page_statistic_create(self):

        self.assertEqual(PageStatistic.objects.count(), 0)

        page = PageFactory(graph_id=PAGE_FANS_ID, likes_count=10, talking_about_count=20)

        self.assertEqual(PageStatistic.objects.count(), 1)

        stat = page.statistics.latest()
        self.assertEqual(stat.likes_count, 10)
        self.assertEqual(stat.talking_about_count, 20)
        self.assertTrue(isinstance(stat.updated_at, datetime))

        page = Page.remote.fetch(PAGE_FANS_ID)

        self.assertEqual(PageStatistic.objects.count(), 2)

        stat = page.statistics.latest()
        self.assertTrue(stat.likes_count > 10)
        self.assertTrue(stat.talking_about_count > 20)
        self.assertTrue(isinstance(stat.updated_at, datetime))

    def test_null_stats_test(self):

        p = PageFactory(likes_count=None, talking_about_count=None)

        self.assertEqual(PageStatistic.objects.count(), 0)
