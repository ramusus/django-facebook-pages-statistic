from django.db import models
from django.utils import timezone

from fbparse import likes_shares_parse


#class FBpageManager(models.Manager):
#
#    def create(self, page):
#        print "create"
#        fbpage = self.model(page=page, **kwargs)
#        fbpage.update()
#        fbpage.save()
#        return fbpage


class FBpage(models.Model):
    page = models.CharField("Page", max_length=64)
    likes = models.PositiveIntegerField(default=0, editable=False)
    shares = models.PositiveIntegerField(default=0, editable=False)
    last_update = models.DateTimeField("Last update time", editable=False,) # default=timezone.now()

    #objects = FBpageManager()

    class Meta:
        verbose_name = "FaceBook page"
        verbose_name_plural = u"FaceBook pages"

    def save(self, *args, **kwargs):
        d = likes_shares_parse(self.page)
        self.likes = d["likes"]
        self.shares = d["shares"]
        self.last_update = timezone.now()

        return super(self.__class__, self).save(*args, **kwargs)





