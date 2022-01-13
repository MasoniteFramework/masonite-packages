"""Task Module Description"""
from masonite.scheduling import Task
import os
import requests
from ..models.Package import Package

from markdown import markdown

class UpdatePackages(Task):
    def handle(self):
        for package in Package.where("is_approved", True).all():
            url = os.path.join(package.pypi_url, "json").replace("/project/", "/pypi/")
            response = requests.get(url)
            if response.status_code != 200:
                print("ERROR: updating package failed !")
                import pdb;pdb.set_trace()
                continue

            data = response.json()
            package.update({"description": markdown(data["info"]["description"])})
