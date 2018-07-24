from orator.migrations import Migration


class FixScheduleLeagueForeignKey(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('schedules') as table:
            table.drop_foreign('schedules_league_id_foreign')
            table.foreign('league_id').references('id').on('leagues') \
                .on_delete('cascade')

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('schedules') as table:
            pass
