""" User Model """

from masoniteorm.models import Model


class Package(Model):
    """Package Model"""

    __fillable__ = ["name",  "short_description", "description", "is_approved", "is_official", "repository_url", "homepage_url", "pypi_url", "stars", "version"]