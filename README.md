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
    After Page (https://github.com/ramusus/django-facebook-pages) created or updated
    page = Page.remote.fetch('19292868552')

    PageStatistic object will be created
    which store likes_count, talking_about_count
    and update time

    ps = PageStatistic.objects.filter(page=page).latest()

    ps.likes_count
    >>>10
    ps.talking_about_count
    >>>20
    ps.updated_at
    >>>datetime.datetime(2014, 10, 28, 15, 12, 16, 128099, tzinfo=<UTC>)

