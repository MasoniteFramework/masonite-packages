"""CreatePackages Migration."""

from masoniteorm.migrations import Migration


class CreatePackages(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("packages") as table:
            table.increments("id")
            table.string("name")
            table.string("slug")
            table.boolean("is_official").default(False)
            table.string("repository_url")
            table.string("homepage_url")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("packages")
