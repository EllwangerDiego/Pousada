class Reserva:
    def __init__(self, dia_inicio: int, dia_fim: int, cliente: str, quarto: str, status: str):
        self.reservas = []
        self.__dia_inicio = dia_inicio
        self.__dia_fim = dia_fim
        self.__cliente = cliente
        self.__quarto = quarto
        self.__status = status

#Utilizando os metodos Getter e Setter
    @property
    def dia_inicio(self) -> int:
        return self.__dia_inicio

    @dia_inicio.setter
    def dia_inicio(self, dia_inicio):
        self.__dia_inicio = dia_inicio

    @property
    def dia_fim(self) -> int:
        return self.__dia_fim
    
    @dia_fim.setter
    def dia_fim(self, dia_fim):
        self.__dia_fim = dia_fim

    @property
    def cliente(self) -> str:
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def quarto(self) -> str:
        return self.__quarto
    
    @quarto.setter
    def quarto(self, quarto):
        self.__quarto = quarto

    @property
    def status(self) -> str:
        return self.__status
    
    @status.setter
    def status(self, status):
        self.__status = status

    def carregar_reservas(self):
        #Carrega as reservas salvas no arquivo

        with open('Reserva.txt', 'r') as f:
            for linha in f:
                nome, quarto, data_inicio, data_fim = linha.strip().split(',')
                self.reservas.append({
                    'nome': nome,
                    'quarto': quarto,
                    'data_inicio': int(data_inicio),
                    'data_fim': int(data_fim)
                })





