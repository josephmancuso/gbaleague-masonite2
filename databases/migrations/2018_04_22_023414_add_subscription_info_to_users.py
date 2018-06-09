from orator.migrations import Migration


class AddSubscriptionInfoToUsers(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('users') as table:
            table.string('customer_id').nullable()
            table.string('plan_id').nullable()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('users') as table:
            pass
