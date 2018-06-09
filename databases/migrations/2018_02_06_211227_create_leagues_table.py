from orator.migrations import Migration


class CreateLeaguesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('leagues') as table:
            table.increments('id')
            table.string('name')
            table.integer('owner_id').unsigned()
            table.foreign('owner_id').references('id').on('users')
            table.text('description').nullable()
            table.string('slug')
            table.integer('tournament').default(0)
            table.integer('current_id').unsigned().nullable()
            table.foreign('current_id').references('id').on('users')
            table.integer('status').default(0)
            table.integer('ordering').default(0)
            table.string('draftorder').nullable()
            table.integer('round').default(1)
            table.string('slackwebhook').nullable()
            table.string('slackchannel').nullable()
            table.string('discordid').nullable()
            table.string('discordtoken').nullable()
            table.string('discordchannel').nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('leagues')
