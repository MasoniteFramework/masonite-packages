from masonite.providers import Provider

from app.tasks.AddNewPackages import AddNewPackages
from app.tasks.UpdatePackages import UpdatePackages
from app.commands.ClearPackagesCommand import ClearPackagesCommand


class PackagesAppProvider(Provider):
    def __init__(self, application):
        self.application = application

    def register(self):
        self.application.make('scheduler').add(
            AddNewPackages().daily_at("09:00")
        )
        self.application.make('scheduler').add(
            UpdatePackages().daily()
        )
        self.application.make("commands").add(ClearPackagesCommand(self.application))

    def boot(self):
        pass
