class Quarto:
    def __init__ (self, numero: int, categoria : str, diaria : float):
        self.__numero = numero
        self.__categoria = categoria
        self.__diaria = diaria
        self.consumo = []

    @property
    def numero(self) -> int:
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def categoria(self) -> str:
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria

    @property
    def diaria(self) -> float:
        return self.__diaria

    @diaria.setter
    def diaria(self, diaria):
        self.__diaria = diaria

    @property
    def consumo(self) -> int:
        return self.__consumo

    @consumo.setter
    def consumo(self, consumo):
        self.__consumo = consumo


