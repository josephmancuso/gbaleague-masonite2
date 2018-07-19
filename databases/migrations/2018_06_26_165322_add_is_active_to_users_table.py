from orator.migrations import Migration


class AddIsActiveToUsersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('users') as table:
            table.integer('is_active').nullable()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('users') as table:
            pass
