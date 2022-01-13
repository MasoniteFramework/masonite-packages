from masonite.controllers import Controller
from masonite.views import View
from masonite.request import Request

from app.models.Package import Package


class PackagesController(Controller):

    def index(self, view: View):
        packages = Package.order_by("is_official", "desc").all()
        return view.render("packages", {"packages": packages})

    def details(self, request:Request, view: View):
        package = Package.where("name", request.param('slug')).first()
        return view.render("package_details", {"package": package})
