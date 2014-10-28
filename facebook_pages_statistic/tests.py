from django.utils import timezone
from django.test import TestCase
from facebook_pages.models import Page

from fbparse import likes_shares_parse
from models import PageStatistic



class ParseTest(TestCase):
    # parse not used in module
    def _test_likes_shares_parse(self):
        d = likes_shares_parse('samsung')
        self.assertIsInstance(d, dict)
        self.assertIn("likes", d)
        self.assertIn("shares", d)
        self.assertIsInstance(d["likes"], int)
        self.assertIsInstance(d["shares"], int)



class PageStatisticTest(TestCase):

    def setUp(self):
        self.t = timezone.now()
        self.p = Page.objects.create(#graph="cocacola",
                    name="cocacola",
                    link="http://facebook.com/cocacola",
                    location="cocacola",
                    cover="cocacola",
                    likes=10,
                    checkins=0,
                    talking_about_count=20,
                    category="cocacola",
                    phone="cocacola",
                    picture="cocacola",
                    website="http://facebook.com/cocacola",
                    username="cocacola",
                    company_overview="cocacola",
                    about="cocacola",
                    products="cocacola",
                    description="cocacola")



    def test_page_statistic_create(self):
        t = self.t
        p = self.p

        ps = PageStatistic.objects.get(id=1)
        self.assertEqual(ps.page, p)
        self.assertEqual(ps.likes, p.likes)
        self.assertEqual(ps.talking_about_count, p.talking_about_count)
        self.assertGreater(ps.updated_at, t)


    def test_test_page_statistic_update(self):
        t = timezone.now()
        p = self.p
        p.likes += 100
        p.talking_about_count += 100
        p.save()

        ps = PageStatistic.objects.get(id=2)
        self.assertEqual(ps.page, p)
        self.assertEqual(ps.likes, p.likes)
        self.assertEqual(ps.talking_about_count, p.talking_about_count)
        self.assertGreater(ps.updated_at, t)
