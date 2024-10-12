#DIEGO ELLWANGER & JOÃO VITOR DALCIN ANDRIOLI

from Reserva import Reserva

class Pousada:
    def __init__(self):
        self.reservas = []

    def carregar_reservas(self):
        #AQUI VAI CARREGAR AS RESERVAS DO ARQUIVO
        try:
            with open('reserva.txt', 'r') as f:
                for linha in f:
                    cliente, quarto, dia_inicio, dia_fim, status = linha.strip().split(',')
                    reserva = Reserva(int(dia_inicio), int(dia_fim), cliente, quarto, status)
                    self.reservas.append(reserva)
        except FileNotFoundError:
            print("Arquivo de reservas não encontrado.")

    def verificar_disponibilidade(self, quarto: str, dia_inicio: int, dia_fim: int) -> bool:
        #FAZ UMA VERIFICAÇÃO DE DISPONIBILIDADE
        for reserva in self.reservas:
            if reserva.quarto == quarto:
                if not (dia_fim < reserva.dia_inicio or dia_inicio > reserva.dia_fim):
                    return False  #QUER DIZER QUE O QUARTO ESTÁ OCUPADO
        return True  #QUARTO DISPONÍVEL

    def realizar_reserva(self, dia_inicio: int, dia_fim: int, cliente: str, quarto: str):
        if self.verificar_disponibilidade(quarto, dia_inicio, dia_fim):
            nova_reserva = Reserva(dia_inicio, dia_fim, cliente, quarto)
            self.reservas.append(nova_reserva)
            print("Reserva realizada com sucesso!")
        else:
            print("Quarto não disponível para as datas selecionadas.")

    def consultar_reserva(self, cliente: str):
        #FAZ UMA CONSULTA EM RELAÇÃO AS RESERVAS DE UM CLIENTE ESPECÍFICO
        for reserva in self.reservas:
            if reserva.cliente == cliente and reserva.status == 'A':
                print(reserva)
                return
        print("Nenhuma reserva ativa encontrada para o cliente.")

    def mudar_status_reserva(self, cliente: str, novo_status: str):
        #MUDA O STATUS DE RESERVA DE UM CLIENTE
        for reserva in self.reservas:
            if reserva.cliente == cliente and reserva.status == 'A':
                reserva._Reserva__status = novo_status 
                print(f'Status da reserva de {cliente} alterado para {novo_status}.')
                return
        print("Nenhuma reserva ativa encontrada para o cliente.")

    def __str__(self):
        return "\n".join(str(reserva) for reserva in self.reservas)


