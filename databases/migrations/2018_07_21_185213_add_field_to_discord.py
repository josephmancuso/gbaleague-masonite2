from orator.migrations import Migration


class AddFieldToDiscord(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('discord') as table:
            table.string('channel_id')
            table.string('token')

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('discord') as table:
            pass
