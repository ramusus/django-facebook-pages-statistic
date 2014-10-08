# -*- coding: utf-8 -*-
from django.contrib import admin
from fb_parse.models import FBpage


class FBpageAdmin(admin.ModelAdmin):
    search_fields = ("page",)
    list_display = ("page", "likes", "shares", "last_update",)


admin.site.register(FBpage, FBpageAdmin)
