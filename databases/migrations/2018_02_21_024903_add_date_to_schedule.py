from orator.migrations import Migration


class AddDateToSchedule(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('schedules') as table:
            table.date('scheduled_for')

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('schedules') as table:
            pass
