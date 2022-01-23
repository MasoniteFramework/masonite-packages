"""Task Module Description"""
from masonite.scheduling import Task
from masoniteorm.exceptions import QueryException

from ..models.Package import Package
from ..pypi import find_packages, get_package_data


class AddNewPackages(Task):

    def handle(self):
        # get list of PyPi packages name with Masonite Framework classifier
        packages = find_packages()

        new_packages = 0
        for package_name in packages:
            # if package already exists don't add it again
            if Package.where("name", package_name).count() == 1:
                continue
            # get additional data for the package
            data = get_package_data(package_name)
            if not data:
                print("ERROR: fetching additional packages details failed !")
                continue

            approved = False
            if data["repository_url"].lower().startswith("https://github.com/masoniteframework/"):
                approved = True
            try:
                Package.create(
                    name=package_name,
                    approved=approved,
                    **data,
                )
            except QueryException as e:
                print(f"ERROR: creating package : {e}")
                continue
            new_packages += 1

        print(f"{new_packages} added !")
