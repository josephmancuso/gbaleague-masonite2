from orator.migrations import Migration


class CreateDraftedPokemonTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('draftedpokemon') as table:
            table.increments('id')
            table.integer('team_id').unsigned()
            table.foreign('team_id').references('id').on('teams')
            table.integer('pokemon_id').unsigned().nullable()
            table.foreign('pokemon_id').references('id').on('pokemon')
            table.integer('queue_id').unsigned().nullable()
            table.foreign('queue_id').references('id').on('pokemon')
            table.integer('league_id').unsigned()
            table.foreign('league_id').references('id').on('leagues')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('draftedpokemon')
