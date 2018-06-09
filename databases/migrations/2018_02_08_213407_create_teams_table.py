from orator.migrations import Migration


class CreateTeamsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('teams') as table:
            table.increments('id')
            table.string('name')
            table.integer('league_id').unsigned().nullable()
            table.foreign('league_id').references('id').on('leagues')
            table.integer('owner_id').unsigned()
            table.foreign('owner_id').references('id').on('users')
            table.integer('points').default(1000)
            table.string('picture').default(1000)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('teams')
