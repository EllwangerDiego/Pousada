#DIEGO ELLWANGER & JOÃO VITOR DALCIN ANDRIOLI

class Reserva:
    def __init__(self, dia_inicio: int, dia_fim: int, cliente: str, quarto: str, status: str = 'A'):
        self.__dia_inicio = dia_inicio
        self.__dia_fim = dia_fim
        self.__cliente = cliente
        self.__quarto = quarto
        self.__status = status

    @property
    def dia_inicio(self) -> int:
        return self.__dia_inicio

    @property
    def dia_fim(self) -> int:
        return self.__dia_fim

    @property
    def cliente(self) -> str:
        return self.__cliente

    @property
    def quarto(self) -> str:
        return self.__quarto

    @property
    def status(self) -> str:
        return self.__status
    
    def verificar_check_in(self):
        return self.__status == 'C'

    def __str__(self):
        return f'Reserva: {self.__cliente} - Quarto: {self.__quarto} - Início: {self.__dia_inicio} - Fim: {self.__dia_fim} - Status: {self.__status}'
