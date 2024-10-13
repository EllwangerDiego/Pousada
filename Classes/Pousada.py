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

    def realiza_checkin(self,cliente:str):
        #realiza o check-in de uma reserva recebendo por parametro o nome de um cliente
        for reserva in self.reservas:
            if reserva.__cliente == cliente and reserva.__status == 'A': #Se a reserva exisitir e for ativa
                reserva.__status = 'I'  #altera o status para check-in e mostra os dados da reserva e do quarto
                print(f'Check-in da reserva de {cliente} realizado com sucesso.')
                print(f'Data inicial: {reserva.__dia_inicio}')
                print(f'Data final: {reserva.__dia_fim}')
                print(f'Dias reservados: {reserva.__dia_fim - reserva.__dia_inicio + 1}')
                print(f'Quarto: {reserva.quarto.__numero}')
                print(f'Categoria do quarto: {reserva.quarto.__categoria}')
                print(f'Valor total das diárias: {reserva.quarto.__diaria * (reserva.__dia_fim - reserva.__dia_inicio + 1)}'                
            else:
                print(f'Nenhuma reserva ativa encontrada para o cliente {cliente}.') 


    def realiza_check_out(self, cliente: str):
        #Verifica se a reserva existe e tem status de check-in
        for reserva in self.reservas:
            if reserva.__cliente == cliente and reserva.__status == 'I':
                #Altera o status da reserva para check-out
                reserva.__status = 'O'
                print(f'Check-out da reserva de {cliente} realizado com sucesso.')
                print(f'Data inicial: {reserva.__dia_inicio}')
                print(f'Data final: {reserva.__dia_fim}')
                print(f'Dias reservados: {reserva.__dia_fim - reserva.__dia_inicio + 1}')
                print(f'Valor total das diárias: {reserva.quarto.__diaria * (reserva.__dia_fim - reserva.__dia_inicio + 1)}')
                                
                #Limpa o consumo do quarto
                reserva.quarto.limpa_consumo()
            else:
                print(f'Nenhuma reserva em check-in encontrada para o cliente {cliente}.')
    
    def __str__(self):
        return "\n".join(str(reserva) for reserva in self.reservas)


