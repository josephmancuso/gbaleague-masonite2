""" A SeedTableCommand Command """
from cleo import Command
from masonite.app import App
from masonite.view import View
from masonite.helpers.filesystem import make_directory
from config.database import DB

class SeedTableCommand(Command):
    """
    Description of command

    seed:table
        {table : Table you want to generate a seed from}
    """

    def handle(self):
        view = View(App())
        class_directory = 'databases/seeds/{}_table_seeder.py'.format(self.argument('table'))

        if not make_directory(class_directory):
            pass
            # return self.error('{0} Seeder Already Exists!'.format(self.argument('table')))


        conn = DB.get_schema_manager().list_table_columns(self.argument('table'))
        # docstring = '"""Model Definition (generated with love by Masonite) \n\n'
        # for name, column in conn.items():
        #     length = '({})'.format(column._length) if column._length else ''
        #     docstring += '{}: {}{} default: {}\n'.format(
        #         name, column.get_type(), length, column.get_default())

        f = open(class_directory, 'w+')
        if view.exists('scaffold/seed'):
            f.write(
                view.render('scaffold/seed', {
                    'table': self.argument('table'),
                    'columns': conn.items(),
                    }).rendered_template
            )
            self.info('Seeder Created Successfully!')
            return f.close()
