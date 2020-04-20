# Using orator
# Github: https://github.com/sdispater/orator
# Official Page: https://orator-orm.com/
# Install via Command Line Interface (CLI): pip install orator

from orator import DatabaseManager, Model

config = {
    'sqlite': {
        'driver': 'sqlite',
        'database': './db/db_teste_pezinho.db',
    }
}

print('Conectando ao Db')

db = DatabaseManager(config)
Model.set_connection_resolver(db)


class Dados(Model):
    pass

print('Retrieving data')
print('--------------')

dados = Dados.all()

for dado in dados:
    print('User: ' + str(dado.id) + " - " + dado.name)
