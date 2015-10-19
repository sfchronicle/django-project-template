import os
import sys

from lib.utils import log
from .other import log_success

from fabric.api import *
from fabric.contrib import django

django.settings_module("{{ project_name }}.settings")
from django.conf import settings

from {{ project_name }}.settings.production import (
    AWS_BUCKET_NAME,
    AWS_MEDIA_BUCKET_NAME,
    AWS_STAGING_BUCKET_NAME,
    VERBOSE_APP_NAME,
    BUILD_DIR
)

"""
Deployment Tasks
================
"""

project_name = "{{ project_name }}"
pwd = os.path.dirname(__file__)
gzip_path = '{0}/{1}/gzip/static/'.format(pwd, project_name)
static_path = '{0}/{1}/static/'.format(pwd, project_name)

@task
def grunt_build():
    """
    Execute grunt build for any cleanup that needs to happen before deploying.
    """
    local('cd {{ project_name }} && grunt build')

@task
def build():
    """shortcut for django bakery build command"""
    local('python manage.py build \
        --skip-static --settings={{ project_name }}.settings.production')

    # hack to move whole directory over to build
    local('cd {} && mv static/* build/'.format(settings.BASE_DIR))

@task
def unbuild():
    """shortcut for django bakery unbuild command"""
    local('python manage.py unbuild \
        --settings={{ project_name }}.settings.production')


@task
def compress():
    """shortcut for django compressor offline compression command"""
    local('python manage.py compress \
        --settings={{ project_name }}.settings.production')


@task
def reset():
    """delete all the deploy code"""
    local('cd {{ project_name }} && \
        rm -rf static && rm -rf gzip && rm -rf build')


@task
def invalidate_buildpath():
    """Invalidate Cloudfront cache when pushed to production"""
    raise NotImplementedError

@task
def s3deploy():
    """Deploy build directory to S3 using aws cli"""
    # using aws cli since boto is busted with buckets that have periods (.) in the name
    local('cd {} && aws s3 cp --recursive --acl public-read build/ s3://{}/{}'.format(
        settings.BASE_DIR, AWS_BUCKET_NAME, VERBOSE_APP_NAME))
    log('Deployed! visit http://{}/{}/\n'.format(AWS_BUCKET_NAME, VERBOSE_APP_NAME), 'green')

@task()
def publish():
    """Compress, build and deploy project to staging bucket on Amazon S3."""
    reset()
    compress()
    build()
    s3deploy()
    log_success()
