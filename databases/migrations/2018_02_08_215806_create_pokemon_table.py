from orator.migrations import Migration


class CreatePokemonTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('pokemon') as table:
            table.increments('id')
            table.string('name')
            table.integer('points')
            table.integer('tier')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('pokemon')
