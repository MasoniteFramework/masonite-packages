"""A HomeController Module."""
from masonite.views import View
from masonite.controllers import Controller

from app.models.Package import Package


class HomeController(Controller):
    """HomeController Controller Class."""

    def home(self, view: View):
        # latest 5 added packages
        last_packages = Package.order_by("created_at", "desc").limit(5).get()
        # best rated packages: TODO: add rate column and order_by
        best_rated_packages = Package.limit(5).get()
        return view.render("home", {"last_packages": last_packages, "best_rated_packages": best_rated_packages})

    def faq(self, view: View):
        return view.render("faq")
