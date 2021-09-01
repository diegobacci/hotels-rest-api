from flask import Flask
#  Em reqparse ele vai receber todas informacoes da requisicao em json
from flask_restful import Api
from resources.hotel import Hoteis, Hotel

app = Flask(__name__)
#  Configuracoes para criacao e execucao do banco - Colocamos o caminho
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Cria na raiz um banco sqlite # Poderiamos mudar o banco para postgress
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Apenas retira notificacoes do sql_alchemy que sobrecarregam
api = Api(app)

#  Decorador
@app.before_first_request
def create_database():  # Verifica se existe um banco
    database.create_all()  # Cria automaticamente o banco e todas as tabelas do "database" no __main__

#  adicionando endpoints
api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:id_hotel>')

if __name__ == '__main__':
    from sql_alchemy import database  # Só importaremos quando o arquivo principal ser chamado
    database.init_app(app)
    app.run(debug=True)