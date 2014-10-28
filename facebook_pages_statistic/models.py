from django.db import models

from facebook_pages.models import Page



class PageStatistic(models.Model):

    page = models.ForeignKey(Page)

    likes = models.PositiveIntegerField(default=0, editable=False)
    talking_about_count = models.PositiveIntegerField(default=0, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, editable=False)


    class Meta:
        verbose_name = "PageStatistic"
        verbose_name_plural = "PageStatistic"
        #get_latest_by = 'updated_at'



import signals
