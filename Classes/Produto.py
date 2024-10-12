class Produto:
    def __init__(self, codigo: int, nome: str, preco: float):
        self.__codigo = codigo  # Código do produto
        self.__nome = nome  # Nome do produto
        self.__preco = preco  # Preço do produto

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    def __str__(self):
        # Retorna uma string formatada com as informações do produto
        return f'Produto: {self.nome}, Código: {self.codigo}, Preço: R$ {self.preco:.2f}'

    @staticmethod
    def serializar(produtos: list):
        # Salva os produtos no arquivo produto.txt
        with open('produto.txt', 'w') as f:
            for produto in produtos:
                f.write(f'{produto.codigo},{produto.nome},{produto.preco:.2f}\n')

    @staticmethod
    def deserializar() -> list:
        # Carrega os produtos do arquivo produto.txt
        produtos = []
        try:
            with open('produto.txt', 'r') as f:
                for linha in f:
                    codigo, nome, preco = linha.strip().split(',')
                    produtos.append(Produto(int(codigo), nome, float(preco)))
        except FileNotFoundError:
            print("Arquivo produto.txt não encontrado. Nenhum produto carregado.")
        return produtos
