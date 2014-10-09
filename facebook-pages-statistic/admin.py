# -*- coding: utf-8 -*-
from django.contrib import admin
from fb_parse.models import PageStatistic


class PageStatisticAdmin(admin.ModelAdmin):
    search_fields = ("page",)
    list_display = ("page", "likes", "shares", "last_update",)


admin.site.register(PageStatistic, PageStatisticAdmin)
