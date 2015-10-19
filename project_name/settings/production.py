import os
from datetime import date

from common import *

DEBUG = False

COMPRESS_ENABLED = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter'
]

COMPRESS_OFFLINE = True
COMPRESS_OUTPUT_DIR = 'prod'

BUILD_DIR = os.path.join(BASE_DIR, 'build')
BAKERY_VIEWS = (
    # Django Bakery Views go here. Example:
    # '{{ project_name }}.apps.some_news_app.views.SomeNewsAppView',
)
AWS_STAGING_BUCKET_NAME = 'staging.projects.sfchronicle.com'
AWS_BUCKET_NAME = 'projects.sfchronicle.com'
AWS_MEDIA_BUCKET_NAME = 'media.projects.sfchronicle.com'

VERBOSE_APP_NAME = '{}/{}'.format(
    date.today().year,
    '{{ project_name }}'
)  # App name in production plus the publish year

STATIC_ROOT = os.path.join(SITE_ROOT, 'static')
STATIC_URL = '{}/{}/{}/'.format(
    "//s3-us-west-1.amazonaws.com",
    AWS_MEDIA_BUCKET_NAME,
    VERBOSE_APP_NAME
)
