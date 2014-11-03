from django.dispatch import receiver
from django.db.models.signals import post_save
from facebook_pages.models import Page
from . models import PageStatistic


@receiver(post_save, sender=Page)
def page_statistic_create(sender, instance, **kwargs):
    if instance.likes_count is None or instance.talking_about_count is None:
        return

    PageStatistic.objects.create(page=instance,
         likes_count=instance.likes_count,
         talking_about_count=instance.talking_about_count)
