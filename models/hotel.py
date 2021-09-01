from sql_alchemy import database

# Classe HotelModel é do tipo banco ==> Determinamos que a classe é uma tabela e atributos são colunas
class HotelModel(database.Model):
    __tablename__ = 'hoteis'

    id_hotel = database.Column(database.String, primary_key=True)  # Transformamos id_hotel em coluna, com tipo e PK
    nome = database.Column(database.String(80))
    estrelas = database.Column(database.Float(precision=1))  # Precisao de uma casa depois da virgula
    valor_diaria = database.Column(database.Float(precision=2))
    cidade = database.Column(database.String(40))


    def __init__(self, id_hotel, nome, estrelas, valor_diaria, cidade):
        self.id_hotel = id_hotel
        self.nome = nome
        self.estrelas = estrelas
        self.valor_diaria = valor_diaria
        self.cidade = cidade

    def json(self):
        return {
            "id_hotel": self.id_hotel,
            "nome": self.nome,
            "estrelas": self.estrelas,
            "valor_diaria": self.valor_diaria,
            "cidade": self.cidade
        }

    # Metodo de classe, pois nao acessara nenhum atributo
    @classmethod
    def find_hotel(cls, id_hotel):  # cls == HotelModel, é uma abreviacao para a classe
        #  SELECT * FROM hoteis WHERE id_hotel = $id_hotel
        hotel = cls.query.filter_by(id_hotel=id_hotel).first()  # Metodo query é nativo do sql_alchemy # Apenas o 1o

