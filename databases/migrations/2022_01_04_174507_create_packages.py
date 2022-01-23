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
            table.string("author")
            table.string("author_email")
            table.text("description", nullable=True)
            table.boolean("is_official").default(False)
            table.boolean("disabled").default(False)
            table.boolean("unmaintained").default(False)
            table.string("version", length=15, nullable=True)
            table.string("pypi_url")
            table.string("repository_url")
            table.string("license").default("N/A")
            # TODO:: how to use enum ?
            table.string("masonite_versions", nullable=True)
            table.integer("stars").default(0)
            table.integer("issues").default(0)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("packages")
