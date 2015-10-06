# -*- coding: utf-8 -*-
'''
Copyright 2011-2015 ramusus
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
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
