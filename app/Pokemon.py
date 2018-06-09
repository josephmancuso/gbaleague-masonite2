''' A Pokemon Database Model '''
from config.database import Model

class Pokemon(Model):
    __table__ = 'pokemon'
