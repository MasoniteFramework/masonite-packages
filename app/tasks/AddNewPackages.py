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
            # get additional data for the package
            data = get_package_data(package_name)
            if not data:
                print("ERROR: fetching additional packages details failed !")
                continue

            approved = False
            if data["repository_url"].startswith("https://github.com/MasoniteFramework/"):
                approved = True
            try:
                Package.create(
                    name=package_name,
                    approved=approved,
                    **data,
                )
            except QueryException as e:
                if str(e) != "UNIQUE constraint failed: packages.name":
                    print(f"ERROR: creating package : {e}")
                continue
            new_packages += 1

        print(f"{new_packages} added !")
