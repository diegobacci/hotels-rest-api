from flask_restful import Resource, reqparse
from models.hotel import HotelModel


class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}


class Hotel(Resource):
    #  Pegamos as informacoes da request do cliente
    argumentos = reqparse.RequestParser()
    #  Determinamos quais sao as chaves de informacoes que queremos receber da request
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('valor_diaria')
    argumentos.add_argument('cidade')

    #  recebe
    def get(self, id_hotel):
        hotel = Hotel.find_hotel(id_hotel)
        if hotel:  # Se existe hotel # if hotel is not None
            return hotel
        return {"message": "Hotel not found."}, 404  # Status code 404 ==> Não encontrado

    #  adiciona
    def post(self, id_hotel):
        if HotelModel.find_hotel(id_hotel):
            return {"message": f"Hotel id {id_hotel} already exists."}, 400  # Requisicao errada

        #  Criamos um construtor onde pegamos todos argumentos com dados da requisicao
        dados = Hotel.argumentos.parse_args()
        objeto_hotel = HotelModel(id_hotel, **dados)  # estamos pegando todos dados do parametro id_hotel passado
        novo_hotel = objeto_hotel.json()
        hoteis.append(novo_hotel)
        return novo_hotel, 200  # Status code 200 ==> Sucesso

    #  altera e cria
    def put(self, id_hotel):
        dados = Hotel.argumentos.parse_args()
        objeto_hotel = HotelModel(id_hotel, **dados)  # estamos pegando todos dados do parametro id_hotel passado
        novo_hotel = objeto_hotel.json()
        hotel = Hotel.find_hotel(id_hotel)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200  # Hotel atualizado # Status code ==> Sucesso
        hoteis.append(novo_hotel)

        return novo_hotel, 201  # Hotel criado # Status code ==> Criado

    def delete(self, id_hotel):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel["id_hotel"] != id_hotel]
        return {"message": "Hotel deleted."}, 200
