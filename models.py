from django.db import models
from django.utils import timezone

from fbparse import likes_shares_parse


class PageStatisticManager(models.Manager):

    def get_with_update(self, *args, **kwargs):
        fbpage = self.get(*args, **kwargs)
        fbpage.save() # calls likes & shares update
        return fbpage


class PageStatistic(models.Model):
    page = models.CharField("Page", max_length=64)
    likes = models.PositiveIntegerField(default=0, editable=False)
    shares = models.PositiveIntegerField(default=0, editable=False)
    last_update = models.DateTimeField("Last update time", editable=False) # default=timezone.now()

    objects = PageStatisticManager()

    def __unicode__(self):
        return self.page

    class Meta:
        verbose_name = "PageStatistic"
        verbose_name_plural = "PageStatistic"

    def save(self, *args, **kwargs):
        d = likes_shares_parse(self.page)
        self.likes = d["likes"]
        self.shares = d["shares"]
        self.last_update = timezone.now()

        return super(self.__class__, self).save(*args, **kwargs)





