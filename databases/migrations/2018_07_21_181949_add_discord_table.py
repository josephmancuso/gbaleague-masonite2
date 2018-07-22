from orator.migrations import Migration


class AddDiscordTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('discord') as table:
            table.increments('id')
            table.string('access_token')
            table.string('refresh_token')
            table.string('scopes')
            table.integer('league_id').unsigned()
            table.foreign('league_id').references('id').on('leagues')
            table.timestamp('expires_at')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('discord')
