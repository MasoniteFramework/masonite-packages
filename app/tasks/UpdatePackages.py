"""Task Module Description"""
from masonite.scheduling import Task

from ..pypi import get_package_data
from ..models.Package import Package


class UpdatePackages(Task):
    def handle(self):
        for package in Package.all():
            # get additional data for the package
            data = get_package_data(package.name)
            if not data:
                print("ERROR: fetching additional packages details failed !")
                continue

            package.update(data)
