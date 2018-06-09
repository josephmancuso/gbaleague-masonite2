from orator.migrations import Migration


class CreateRequestsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('requests') as table:
            table.increments('id')
            table.integer('team_id').unsigned()
            table.foreign('team_id').references('id').on('teams')
            table.integer('league_id').unsigned()
            table.foreign('league_id').references('id').on('leagues')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('requests')
