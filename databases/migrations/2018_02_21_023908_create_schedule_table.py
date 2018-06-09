from orator.migrations import Migration


class CreateScheduleTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('schedules') as table:
            table.increments('id')
            table.integer('league_id').unsigned()
            table.integer('team1_id').unsigned()
            table.integer('team2_id').unsigned()
            table.integer('winner_id').unsigned().nullable()
            
            table.foreign('league_id').references('id').on('leagues')
            table.foreign('team1_id').references('id').on('teams')
            table.foreign('team2_id').references('id').on('teams')
            table.foreign('winner_id').references('id').on('teams')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('schedules')
