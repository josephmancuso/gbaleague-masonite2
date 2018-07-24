from orator.migrations import Migration


class FixTeamLeagueForeignKey(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('teams') as table:
            table.drop_foreign('teams_league_id_foreign')
            table.foreign('league_id').references('id').on('leagues') \
                .on_delete('SET NULL')

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('teams') as table:
            pass
