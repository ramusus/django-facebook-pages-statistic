# -*- coding: utf-8 -*-
from django.utils import timezone
from facebook_pages.factories import PageFactory
from models import PageStatistic
import factory
import random


class PageStatisticFactory(factory.DjangoModelFactory):
    FACTORY_FOR = PageStatistic

    page = factory.SubFactory(PageFactory)
    likes_count = factory.LazyAttribute(lambda o: random.randint(0, 10000))
    talking_about_count = factory.LazyAttribute(lambda o: random.randint(0, 10000))
    updated_at = factory.LazyAttribute(lambda o: timezone.now())
