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

    @property
    def categoria(self):
        return self.__categoria

    @property
    def diaria(self):
        return self.__diaria

    @property
    def consumo(self):
        return self.__consumo

    def carregar_produtos(self):
        #Carrega os produtos disponíveis a partir do arquivo produto.txt
        produtos = {}
        try:
            with open('produto.txt', 'r') as arquivo:
                for linha in arquivo:
                    nome, preco = linha.strip().split(',')
                    produtos[nome] = float(preco)
        except FileNotFoundError:
            print("Arquivo de produtos não encontrado.")
        return produtos

    def adiciona_consumo(self, produto: str):
        #Registra o consumo do produto.
        if produto in self.produtos_disponiveis:
            valor = self.produtos_disponiveis[produto]
            self.__consumo.append((produto, valor))
            print(f'Produto {produto} adicionado ao consumo do quarto {self.numero}.')
        else:
            print(f'Produto {produto} não disponível.')

    def lista_consumo(self):
        #Lista os produtos consumidos.
        if not self.__consumo:
            print(f'Nenhum consumo registrado para o quarto {self.numero}.')
            return
        print(f'Consumo do quarto {self.numero}:')
        for produto, valor in self.__consumo:
            print(f'- {produto}: R$ {valor:.2f}')

    def valor_total_consumo(self) -> float:
        #Calcula o valor total do consumo.
        total = sum(valor for _, valor in self.__consumo)
        print(f'Valor total do consumo do quarto {self.numero}: R$ {total:.2f}')
        return total

    def limpa_consumo(self):
        #Limpa o consumo do quarto.
        self.__consumo.clear()
        print(f'O consumo do quarto {self.numero} foi limpo.')

    def serializar(self):
        #Serializa os dados do quarto para um formato de texto.
        dados_quarto = f'{self.numero},{self.categoria},{self.diaria}\n'
        dados_consumo = ''.join([f'{item[0]},{item[1]}\n' for item in self.__consumo])
        return dados_quarto + dados_consumo

    @staticmethod
    def deserializar(linha: str):
        #Deserializa os dados do quarto a partir de uma linha de texto.
        dados = linha.strip().split(',')
        numero = int(dados[0])
        categoria = dados[1]
        diaria = float(dados[2])
        novo_quarto = Quarto(numero, categoria, diaria)
        # Registra o consumo se houver
        for i in range(3, len(dados), 2):
            produto = dados[i]
            valor = float(dados[i + 1])
            novo_quarto.adiciona_consumo(produto)
        return novo_quarto

    def salvar_quarto(self):
        #Salva os dados do quarto no arquivo quarto.txt
        with open('quarto.txt', 'a') as f:
            f.write(self.serializar())

    @staticmethod
    def carregar_quartos():
        #Carrega os quartos do arquivo quarto.txt
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
        #Retorna uma string formatada com as informações do quarto
        consumo_str = ', '.join([f'{item[0]}: R$ {item[1]:.2f}' for item in self.__consumo])
        if not consumo_str:
            consumo_str = 'Nenhum consumo registrado.'
        return (f'Quarto {self.numero} - Categoria: {self.categoria}, Diária: R$ {self.diaria:.2f}\n'
                f'Consumo: {consumo_str}')
