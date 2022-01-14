from tkinter import Pack
from masonite.commands import Command
from ..models.Package import Package


class ClearPackagesCommand(Command):
    """
    Clear all Masonite packages from database.

    masonite-packages:clear
    """

    def __init__(self, application):
        super().__init__()
        self.app = application

    def handle(self):
        # do whatever you want !
        for p in Package.all():
            p.delete()
        self.info("All packages have been deleted !")
