from masonite.controllers import Controller
from masonite.views import View
from masonite.request import Request

from app.models.Package import Package


class PackagesController(Controller):

    def index(self, view: View):
        packages = Package.where("disabled", False).order_by("is_official", "desc").order_by("stars", "desc").all()
        return view.render("packages", {"packages": packages})

    def details(self, request:Request, view: View):
        package = Package.where("disabled", False).where("name", request.param('slug')).first()
        return view.render("package_details", {"package": package})
