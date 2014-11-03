from django.db import models
from facebook_pages.models import Page


class PageStatistic(models.Model):
    class Meta:
        verbose_name = "Facebook page statistic"
        verbose_name_plural = "Facebook page statistics"
        get_latest_by = 'id'

    page = models.ForeignKey(Page, related_name='statistics')

    likes_count = models.PositiveIntegerField(editable=False)
    talking_about_count = models.PositiveIntegerField(editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, editable=False)

import signals
