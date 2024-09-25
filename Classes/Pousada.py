from reserva import Reserva

class Pousada:
    def __init__(self,nome:str,contato:str):
        self.nome     = nome
        self.contato  = contato
        self.quartos  = []
        self.reservas = []
        self.produtos = []


def cancela_reserva (nome_cliente):
    for reserva in self.reservas:
        if reserva.get.cliente() == nome_cliente and reserva.get.status() == 'A':
            reserva.status = 'C'
            print(f"Reserva de {nome_cliente} cancelada com sucesso! \n ")
        else:
            print(f"Não existem reservas no nome de {nome_cliente}")
