#DIEGO ELLWANGER & JOÃO VITOR DALCIN ANDRIOLI

from .Produto import Produto

class Quarto:
    def __init__(self, numero: int, categoria: str, diaria: float):
        self.__numero = numero
        self.__categoria = categoria  # 'S' para Standard, 'M' para Master, 'P' para Premium
        self.__diaria = diaria
        self.__consumo = [] 
        self.produtos_disponiveis = self.carregar_produtos()  #CARREGA OS PRODUTOS DO ARQUIVO

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria

    @property
    def diaria(self):
        return self.__diaria
    
    @diaria.setter
    def diaria(self, diaria):
        self.__diaria = diaria

    @property
    def consumo(self):
        return self.__consumo
    
    @consumo.setter
    def consumo(self, consumo):
        self.__consumo = consumo

    
    def carregar_produtos(self):
        #CARREGA OS PRODUTOS DO ARQUIVO "produto.txt"
        consumo = []
        try:
            with open('produto.txt', 'r') as arquivo:
                for linha in arquivo:
                    codigo, nome, preco = linha.strip().split(',')
                    consumo.append(Produto(int(codigo), nome, float(preco)))
        except FileNotFoundError:
            print("Arquivo produto.txt não encontrado. Nenhum produto carregado.")
        return consumo
    #DEVOLVE EM UMA LISTA "consumo", para mais fáci manipulação

    def adiciona_consumo(self, produto: str):
        #REGISTRA O CONSUMO DO PRODUTO
        if produto in self.produtos_disponiveis:
            valor = self.produtos_disponiveis[produto]
            self.__consumo.append((produto, valor))
            print(f'Produto {produto} adicionado ao consumo do quarto {self.numero}.')
        else:
            print(f'Produto {produto} não disponível.')

    def lista_consumo(self):
        #LISTA OS PRODUTOS CONSUMIDOS
        if not self.__consumo:
            print(f'Nenhum consumo registrado para o quarto {self.numero}.')
            return
        print(f'Consumo do quarto {self.numero}:')
        for produto, valor in self.__consumo:
            print(f'- {produto}: R$ {valor:.2f}')

    def valor_total_consumo(self) -> float:
        #CALCULA O VALOR TOTAL DO CONSUMO
        total = sum(valor for _, valor in self.__consumo)
        print(f'Valor total do consumo do quarto {self.numero}: R$ {total:.2f}')
        return total

    def limpa_consumo(self):
        #LIMPA O CONSUMO DO QUARTO
        self.__consumo.clear()
        print(f'O consumo do quarto {self.numero} foi limpo.')

    def serializar(self):
        #SERIALIZA PARA UM FORMATO DE TEXTO
        dados_quarto = f'{self.numero},{self.categoria},{self.diaria}\n'
        dados_consumo = ''.join([f'{item[0]},{item[1]}\n' for item in self.__consumo])
        return dados_quarto + dados_consumo

    @staticmethod
    def deserializar(linha: str):
        #DESERIALIZA OS DADOS
        dados = linha.strip().split(',')
        numero = int(dados[0])
        categoria = dados[1]
        diaria = float(dados[2])
        novo_quarto = Quarto(numero, categoria, diaria)
        #REGISTRA O CONSUMO
        for i in range(3, len(dados), 2):
            produto = dados[i]
            valor = float(dados[i + 1])
            novo_quarto.adiciona_consumo(produto)
        return novo_quarto

    def salvar_quarto(self):
        #SALVA OS DADOS NO ARQUIVO "quarto.txt"
        with open('quarto.txt', 'a') as f:
            f.write(self.serializar())

    @staticmethod
    def carregar_quartos():
        #CARREGA OS QUARTOS DO ARQUIVO "quarto.txt"
        quartos = []
        try:
            with open('quarto.txt', 'r') as f:
                for linha in f:
                    quarto = Quarto.deserializar(linha)
                    quartos.append(quarto)
        except FileNotFoundError:
            print('Arquivo de quartos não encontrado.')
        return quartos

    def __str__(self):
        #RETORNA UMA STRING FORMATADA COM AS INFOS DO QUARTO
        consumo_str = ', '.join([f'{item[0]}: R$ {item[1]:.2f}' for item in self.__consumo])
        if not consumo_str:
            consumo_str = 'Nenhum consumo registrado.'
        return (f'Quarto {self.numero} - Categoria: {self.categoria}, Diária: R$ {self.diaria:.2f}\n'
                f'Consumo: {consumo_str}')
