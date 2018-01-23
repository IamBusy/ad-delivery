from orator.migrations import Migration


class CreateCreativesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('creatives') as table:
            table.big_increments('id')
            table.medium_integer('type').default(1)
            table.string('title')
            table.string('category_name1').nullable()
            table.string('category_name2').nullable()
            table.string('category_name3').nullable()
            table.soft_deletes()
        pass

    def down(self):
        """
        Revert the migrations.
        """
        pass
