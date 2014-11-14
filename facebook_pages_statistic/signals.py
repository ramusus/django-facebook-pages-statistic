from django.dispatch import receiver
from facebook_api.signals import facebook_api_post_fetch
from facebook_pages.models import Page
from . models import PageStatistic


@receiver(facebook_api_post_fetch, sender=Page)
def page_statistic_create(sender, instance, **kwargs):
    PageStatistic.objects.create(page=instance,
         likes_count=instance.likes_count,
         talking_about_count=instance.talking_about_count)
