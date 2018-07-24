from orator.migrations import Migration


class FixLeagueDiscordForeignKey(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('discord') as table:
            table.drop_foreign('discord_league_id_foreign')
            table.foreign('league_id').references('id').on('leagues') \
                .on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        pass
