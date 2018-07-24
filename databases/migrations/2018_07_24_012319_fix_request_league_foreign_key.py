from orator.migrations import Migration


class FixRequestLeagueForeignKey(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('requests') as table:
            table.drop_foreign('requests_league_id_foreign')
            table.foreign('league_id').references('id').on('leagues') \
                .on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('requests') as table:
            pass
