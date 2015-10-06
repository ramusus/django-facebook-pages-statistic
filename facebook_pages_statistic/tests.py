'''
Copyright 2011-2015 ramusus
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
from datetime import datetime

from django.test import TestCase
from facebook_api.signals import facebook_api_post_fetch
from facebook_pages.factories import PageFactory
from facebook_pages.models import Page
from .models import PageStatistic

PAGE_FANS_ID = 19292868552


class FacebookPagesStatisticTest(TestCase):
    def test_page_statistic_create(self):
        self.assertEqual(PageStatistic.objects.count(), 0)

        page = PageFactory(graph_id=PAGE_FANS_ID, likes_count=10, talking_about_count=20)

        self.assertEqual(PageStatistic.objects.count(), 0)

        facebook_api_post_fetch.send(sender=page.__class__, instance=page, created=True)

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
        page = PageFactory(likes_count=None, talking_about_count=None)
        facebook_api_post_fetch.send(sender=page.__class__, instance=page, created=True)

        self.assertEqual(PageStatistic.objects.count(), 0)
