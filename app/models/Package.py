""" User Model """

from masoniteorm.models import Model


class Package(Model):
    """Package Model"""

    __fillable__ = ["name", "slug", "is_official", "repository_url", "homepage_url",]
