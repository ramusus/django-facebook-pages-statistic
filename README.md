# Django Facebook Pages Statistic

[![Build Status](https://travis-ci.org/ramusus/django-facebook-pages-statistic.png?branch=master)](https://travis-ci.org/ramusus/django-facebook-pages-statistic) [![Coverage Status](https://coveralls.io/repos/ramusus/django-facebook-pages/badge.png?branch=master)](https://coveralls.io/r/ramusus/django-facebook-pages-statistic)

Application for storing Facebook Pages statistic (likes and talking_about counters) for different timesnaps

## Installation

    pip install facebook-pages-statistic

Add into `settings.py` lines:

    INSTALLED_APPS = (
        ...
        'taggit',
        'oauth_tokens',
        'facebook_api',
        'facebook_pages',
        'facebook_pages_statistic',
    )

    # oauth-tokens settings
    OAUTH_TOKENS_HISTORY = True                                        # to keep in DB expired access tokens
    OAUTH_TOKENS_FACEBOOK_CLIENT_ID = ''                               # application ID
    OAUTH_TOKENS_FACEBOOK_CLIENT_SECRET = ''                           # application secret key
    OAUTH_TOKENS_FACEBOOK_SCOPE = ['offline_access']                   # application scopes
    OAUTH_TOKENS_FACEBOOK_USERNAME = ''                                # user login
    OAUTH_TOKENS_FACEBOOK_PASSWORD = ''                                # user password

## Usage examples

After Page (https://github.com/ramusus/django-facebook-pages) created or updated
PageStatistic instance will be created which store likes_count, talking_about_count and update time

    >>> page = Page.remote.fetch('19292868552')
    >>> stat = page.statistics.latest()
    >>> stat.likes_count
    10
    >>> stat.talking_about_count
    20
    >>> stat.updated_at
    datetime.datetime(2014, 10, 28, 15, 12, 16, 128099, tzinfo=<UTC>)

