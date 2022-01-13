"""Task Module Description"""
import requests

from masonite.environment import env
from masonite.scheduling import Task
from masoniteorm.exceptions import QueryException

from ..blacklist import REPOS_BLACKLIST
from ..models.Package import Package


class AddNewPackages(Task):
     def handle(self):
        print("starting task !!!")
        url = f"https://libraries.io/api/search?platforms=Pypi&keywords=Masonite,masonite&api_key={env('LIBRARIES_IO_API_KEY')}"
        response = requests.get(url)
        if response.status_code != 200:
            print("ERROR: fetching packages failed !")

        data = response.json()
        for repo in data:
            # avoid adding packages which are not
            if repo["repository_url"] not in REPOS_BLACKLIST:
                # add new packages only : done through unique flag
                is_official = False
                approved = False
                if repo["repository_url"].startswith("https://github.com/MasoniteFramework/"):
                    is_official = True
                    approved = True
                try:
                    Package.create(
                        name=repo["name"],
                        short_description=repo["description"] or "N/A",
                        description=repo["description"] or "N/A",
                        homepage_url=repo["homepage"],
                        repository_url=repo["repository_url"],
                        version=repo["latest_stable_release_number"],
                        pypi_url=repo["package_manager_url"],
                        approved=approved,
                        is_official=is_official,
                        stars=repo["stars"]
                    )
                except QueryException:
                    # UNIQUE
                    pass
        pass
