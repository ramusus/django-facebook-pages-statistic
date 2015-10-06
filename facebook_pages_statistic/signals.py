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
from django.dispatch import receiver
from facebook_api.signals import facebook_api_post_fetch
from facebook_pages.models import Page

from .models import PageStatistic


@receiver(facebook_api_post_fetch, sender=Page)
def page_statistic_create(sender, instance, **kwargs):
    if instance.likes_count is None and instance.talking_about_count is None:
        return

    PageStatistic.objects.create(page=instance,
                                 likes_count=instance.likes_count,
                                 talking_about_count=instance.talking_about_count)
