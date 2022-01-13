"""CreatePackages Migration."""

from masoniteorm.migrations import Migration


class CreatePackages(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("packages") as table:
            table.increments("id")
            table.string("name").unique()
            table.string("short_description")
            table.long_text("description", nullable=True)
            table.boolean("is_official").default(False)
            table.boolean("is_approved").default(False)
            table.string("version", length=15, nullable=True)
            table.string("pypi_url")
            table.string("repository_url")
            table.string("homepage_url")
            table.integer("stars")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("packages")
