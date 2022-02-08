""" Package Model """
from masoniteorm.models import Model


class Package(Model):
    """Package Model"""

    __fillable__ = [
        "name",
        "author",
        "author_email",
        "short_description",
        "description",
        "disabled",
        "is_official",
        "repository_url",
        "homepage_url",
        "pypi_url",
        "stars",
        "version"
    ]

    __append__ = ["last_update"]

    @property
    def last_update(self):
        return self.updated_at.to_datetime_string()

