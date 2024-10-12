from Reserva import Reserva

class Pousada:
    def __init__(self):
        self.reservas = []

    def carregar_reservas(self):
        # Carregar reservas do arquivo
        try:
            with open('reserva.txt', 'r') as f:
                for linha in f:
                    cliente, quarto, dia_inicio, dia_fim, status = linha.strip().split(',')
                    reserva = Reserva(int(dia_inicio), int(dia_fim), cliente, quarto, status)
                    self.reservas.append(reserva)
        except FileNotFoundError:
            print("Arquivo de reservas não encontrado.")

    def verificar_disponibilidade(self, quarto: str, dia_inicio: int, dia_fim: int) -> bool:
        # Verifica se o quarto está disponível para as datas fornecidas
        for reserva in self.reservas:
            if reserva.quarto == quarto:
                if not (dia_fim < reserva.dia_inicio or dia_inicio > reserva.dia_fim):
                    return False  # Quarto está ocupado
        return True  # Quarto está disponível

    def realizar_reserva(self, dia_inicio: int, dia_fim: int, cliente: str, quarto: str):
        if self.verificar_disponibilidade(quarto, dia_inicio, dia_fim):
            nova_reserva = Reserva(dia_inicio, dia_fim, cliente, quarto)
            self.reservas.append(nova_reserva)
            print("Reserva realizada com sucesso!")
        else:
            print("Quarto não disponível para as datas selecionadas.")

    def consultar_reserva(self, cliente: str):
        # Consultar reservas de um cliente específico
        for reserva in self.reservas:
            if reserva.cliente == cliente and reserva.status == 'A':
                print(reserva)
                return
        print("Nenhuma reserva ativa encontrada para o cliente.")

    def mudar_status_reserva(self, cliente: str, novo_status: str):
        # Mudar o status da reserva do cliente
        for reserva in self.reservas:
            if reserva.cliente == cliente and reserva.status == 'A':
                reserva._Reserva__status = novo_status  # Muda o status da reserva diretamente
                print(f'Status da reserva de {cliente} alterado para {novo_status}.')
                return
        print("Nenhuma reserva ativa encontrada para o cliente.")

    def __str__(self):
        return "\n".join(str(reserva) for reserva in self.reservas)


