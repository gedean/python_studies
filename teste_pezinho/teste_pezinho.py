from orator import DatabaseManager, Model

config = {
    'sqlite': {
        'driver': 'sqlite',
        'database': './Testedopezinho.db',
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


