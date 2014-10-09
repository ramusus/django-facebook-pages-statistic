from django.db import models
from django.utils import timezone

from fbparse import likes_shares_parse
from facebook_pages.models import Page




class PageManager(models.Manager):

    def get_with_updated_stats(self, *args, **kwargs):
        page = self.get(*args, **kwargs)
        page.update_stats()
        return page




class Page(Page):

    objects = PageManager()

    def update_stats(self):
        self.pagestatistic_set.create()
        return self

    @property
    def last_stats(self):
        return self.pagestatistic_set.latest()


    class Meta(Page.Meta):
        proxy = True
        #app_label = 'facebook_pages'



#class PageStatisticManager(models.Manager):
#
#    def get_with_update(self, *args, **kwargs):
#        fbpage = self.get(*args, **kwargs)
#        fbpage.save() # calls likes & shares update
#        return fbpage


class PageStatistic(models.Model):
    #page = models.CharField("Page", max_length=64)
    page = models.ForeignKey(Page)

    likes = models.PositiveIntegerField(default=0, editable=False)
    shares = models.PositiveIntegerField(default=0, editable=False)
    last_update = models.DateTimeField("Last update time", editable=False, auto_now_add=True)

    #objects = PageStatisticManager()

#    def __unicode__(self):
#        return self.page

    class Meta:
        verbose_name = "PageStatistic"
        verbose_name_plural = "PageStatistic"
        get_latest_by = 'last_update'

    def save(self, *args, **kwargs):
        page = self.page.name
        d = likes_shares_parse(page)
        self.likes = d["likes"]
        self.shares = d["shares"]

        return super(self.__class__, self).save(*args, **kwargs)





