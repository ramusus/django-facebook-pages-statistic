# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import PageStatistic


class PageStatisticAdmin(admin.ModelAdmin):
    search_fields = ("page",)
    list_display = ("page", "likes_count", "talking_about_count", "updated_at",)


admin.site.register(PageStatistic, PageStatisticAdmin)
