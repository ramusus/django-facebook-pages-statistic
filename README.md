# Django Facebook Pages Statistic

Extends https://github.com/ramusus/django-facebook-pages
add likes and shares parse for FB pages


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


## Usage examples
    First create page
    see https://github.com/ramusus/django-facebook-pages

    supose what we already have page with name 'cocacola'

    >>> from facebook_pages_statistic.models import Page
    >>> p = Page.objects.get_with_updated_stats(name='cocacola')
    >>> p.last_stats.likes
    89131588
    >>> p.last_stats.shares
    927945

