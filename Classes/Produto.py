#DIEGO ELLWANGER & JOÃO VITOR DALCIN ANDRIOLI

class Produto:
    def __init__(self, codigo: int, nome: str, preco: float):
        self.__codigo = codigo  # Código do produto
        self.__nome = nome  # Nome do produto
        self.__preco = preco  # Preço do produto
    

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    def __str__(self):
        #RETORNA UMA STRING FORMATADA COM AS INFOS DO PRODUTO
        return f'Código: {self.codigo}, Produto: {self.nome}, Preço: R$ {self.preco:.2f}'

    @staticmethod
    def serializar(produtos: list):
        #SALVA OS PRODUTOS NO ARQUIVO "produto.txt"
        with open('produto.txt', 'w') as f:
            for produto in produtos:
                f.write(f'{produto.codigo},{produto.nome},{produto.preco:.2f}\n')

    @staticmethod
    def deserializar() -> list:
        #CARREGA OS PRODUTOS DO ARQUIVO "produto.txt"
        produtos = []
        try:
            with open('produto.txt', 'r') as f:
                for linha in f:
                    codigo, nome, preco = linha.strip().split(',')
                    produtos.append(Produto(int(codigo), nome, float(preco)))
        except FileNotFoundError:
            print("Arquivo produto.txt não encontrado. Nenhum produto carregado.")
        return produtos
    #DEVOLVE EM UMA LISTA "produtos", para mais fáci manipulação
