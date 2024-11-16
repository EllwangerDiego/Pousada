#DIEGO ELLWANGER & JOÃO VITOR DALCIN ANDRIOLI

import time
from .Reserva import Reserva
from .Produto import Produto
from .Quarto import Quarto


class Pousada:
    def __init__(self, nome: str, contato: str):
        self.__nome = nome  # Nome da pousada
        self.__contato = contato  # Contato da pousada
        self.__quartos = []  # Lista de objetos Quarto
        self.__reservas = []  # Lista de objetos Reserva
        self.__produtos = []  # Lista de objetos Produto
        self.carrega_dados()  # Carregar dados ao iniciar

    def carrega_dados(self):
        # Carrega os dados dos arquivos
        self.carregar_quartos()
        self.carregar_reservas()
        self.carregar_produtos()
        self.carregar_pousada() 

    def carregar_quartos(self):
        try:
            with open("quarto.txt", "r") as file:
                for linha in file:
                    # Ignora linhas vazias
                    linha = linha.strip()  # Remove espaços em branco ao redor
                    if not linha:  # Se a linha estiver vazia, continua para a próxima
                        continue
                    
                    
                    try:
                        numero, categoria, diaria = linha.split(',')
                        # Certifique-se de que está convertendo 'diaria' para um tipo apropriado
                        numero = int(numero)  # Converte o número do quarto para int
                        diaria = float(diaria)  # Converte a diária para float

                        # Criação do objeto Quarto e adição à lista
                        novo_quarto = Quarto(numero, categoria, diaria)
                        self.__quartos.append(novo_quarto)

                    except ValueError as e:
                        print(f"Erro ao processar a linha: '{linha}': {e}")

        except Exception as e:
            print(f"Erro ao carregar quartos: {e}")

    def carregar_reservas(self):
        try:
            with open("reserva.txt", "r") as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(',')
                    numero_quarto = int(dados[0])
                    cliente = dados[1].strip()
                    
                    # Converte a data de formato 'DD/MM/AAAA' para um inteiro
                    dia_inicio = int(dados[2].replace('/', ''))  # Por exemplo: '06/02/2006' para 6022006
                    dia_fim = int(dados[3].replace('/', ''))  # Exemplo: '10/02/2006' para 10022006
                    
                    # Adiciona o status
                    status = dados[4].strip()  # O status é o quinto elemento

                    quarto = self.encontrar_quarto_por_numero(numero_quarto)  
                    if quarto:
                        # Passa o status para a instância da reserva
                        reserva = Reserva(dia_inicio, dia_fim, cliente, quarto, status)
                        self.__reservas.append(reserva)
                    else:
                        print(f"Quarto {numero_quarto} não encontrado.")
        except FileNotFoundError:
            print("Arquivo de reservas não encontrado.")
        except ValueError as e:
            print(f"Erro ao processar a linha: '{linha}'. Erro: {e}")


    def encontrar_quarto_por_numero(self, numero: int):
        for quarto in self.__quartos: 
            if quarto.numero == numero:
                return quarto
        return None  # Retorna None se o quarto não for encontrado

    def carregar_produtos(self):
        # Carrega os produtos do arquivo "produto.txt"
        try:
            with open('produto.txt', 'r') as arquivo:
                for linha in arquivo:
                    # Supondo que o formato do arquivo seja "codigo,nome,preco"
                    codigo, nome, preco = linha.strip().split(',')
                    produto = Produto(int(codigo), nome, float(preco))
                    self.__produtos.append(produto)
        except FileNotFoundError:
            print("Arquivo produto.txt não encontrado. Nenhum produto carregado.")

    def carregar_pousada(self):
        # Carrega os dados da pousada do arquivo "pousada.txt"
        try:
            with open('pousada.txt', 'r') as arquivo:
                for linha in arquivo:
                    # Supondo que o formato do arquivo seja "nome,contato"
                    nome, contato = linha.strip().split(',')
                    self.__nome = nome
                    self.__contato = contato
        except FileNotFoundError:
            print("Arquivo pousada.txt não encontrado. Nenhum dado da pousada carregado.")



    def consulta_disponibilidade(self, data: str, quarto_numero: int):
    # Converte a data de string para int
        data_int = int(data.replace('/', ''))  # Por exemplo: '06/02/2006' para 6022006

        for reserva in self.__reservas:
            if reserva.quarto.numero == quarto_numero and reserva.status == 'A':  # Verifica se a reserva é ativa
                if reserva.dia_inicio <= data_int <= reserva.dia_fim:  # Comparação
                    print(f"\nO quarto {quarto_numero} não está disponível na data {data}.")
                    time.sleep(2)
                    return False

        print(f"\nO quarto {quarto_numero} está disponível na data {data}.")
        time.sleep(2)
        return True

    # + salva_dados()
    def salva_dados(self):
    # Filtra e salva as reservas que não estão canceladas (C) ou com check-out (O)
        try:
            with open("reserva.txt", "r") as arquivo_reservas:
                reservas = arquivo_reservas.readlines()
        except FileNotFoundError:
            print("Arquivo de reservas não encontrado.")
            return

        # Lista para armazenar as reservas válidas
        reservas_validas = []

        for linha in reservas:
            dados = linha.strip().split(',')
            status = dados[4].strip()

            # Mantém apenas reservas ativas (A) ou em check-in (I)
            if status == 'A' or status == 'I':
                reservas_validas.append(linha)

        # Reescreve o arquivo de reservas apenas com as reservas válidas
        with open("reserva.txt", "w") as arquivo_reservas:
            arquivo_reservas.writelines(reservas_validas)

        print("Dados de reservas salvos com sucesso, excluindo reservas canceladas ou finalizadas.")

        # Agora, faz a mesma coisa para os quartos
        try:
            with open("quarto.txt", "r") as arquivo_quartos:
                quartos = arquivo_quartos.readlines()
        except FileNotFoundError:
            print("Arquivo de quartos não encontrado.")
            return

        # Reescreve o arquivo para salvar
        with open("quarto.txt", "w") as arquivo_quartos:
            arquivo_quartos.writelines(quartos)

        print("Dados dos quartos salvos com sucesso.")
        time.sleep(2)

        


    # + consulta_reserva(data, cliente, quarto)
    def consulta_reserva(self, data: str, cliente: str, quarto_numero: int):
    # Converte a data de string para int
        data_int = int(data.replace('/', ''))  # Por exemplo: '06/02/2006' para 6022006

        for reserva in self.__reservas:
            if reserva.quarto.numero == quarto_numero and reserva.cliente == cliente:
                if reserva.dia_inicio <= data_int <= reserva.dia_fim:
                
                    print(f"\nReserva encontrada: {cliente} no quarto {quarto_numero} na data {data}.")
                    time.sleep(2)
                    return reserva
        print("Nenhuma reserva encontrada para os dados informados.")
        return None

    # + realiza_reserva
    def realiza_reserva(self, dia_inicio: str, dia_fim: str, cliente: str, numero_quarto: int, status = 'A'):
        # Verifica se o quarto está disponível nas datas informadas
        if not self.consulta_disponibilidade(dia_inicio.replace('/', ''), numero_quarto):  # Verifica sem as barras
            print(f"O quarto {numero_quarto} não está disponível entre {dia_inicio} e {dia_fim}.")
            return  # Não realiza a reserva se o quarto não estiver disponível
        
        # Formata a string da reserva no formato correto, mantendo as barras
        reserva_formatada = f"{numero_quarto},{cliente},{dia_inicio},{dia_fim},{status}\n"
        
        # Salva a reserva no arquivo
        with open('reserva.txt', 'a') as arquivo:
            arquivo.write(reserva_formatada)  # Adiciona a reserva no final do arquivo
        
        print("Reserva realizada com sucesso!")
        time.sleep(2)

    # + cancela_reserva
    def cancela_reserva(self, cliente: str):
        reserva_encontrada = False
        reservas_atualizadas = []

        # Lê as reservas do arquivo
        try:
            with open("reserva.txt", "r") as arquivo:
                reservas_atualizadas = arquivo.readlines()
        except FileNotFoundError:
            print("Arquivo de reservas não encontrado.")
            return
        time.sleep(2)

        # Atualiza o status da reserva
        for i, linha in enumerate(reservas_atualizadas):
            dados = linha.strip().split(',')
            numero_quarto = int(dados[0])
            cliente_reserva = dados[1].strip()
            dia_inicio = dados[2]
            dia_fim = dados[3]
            status = dados[4]

            # Verifica se a reserva é a do cliente e está ativa
            if cliente_reserva == cliente and status == 'A':
                reservas_atualizadas[i] = f"{numero_quarto},{cliente_reserva},{dia_inicio},{dia_fim},C\n"  # Muda o status para 'C'
                reserva_encontrada = True
                print(f"A reserva do cliente {cliente} foi cancelada com sucesso.")
                break

        if not reserva_encontrada:
            print(f"Não foi encontrada reserva ativa para o cliente {cliente}.")
        else:
            # Salva as reservas atualizadas no arquivo
            with open("reserva.txt", "w") as arquivo:
                arquivo.writelines(reservas_atualizadas)  # Escreve todas as reservas de volta no arquivo
        
        
        

    # + realiza_checkin
    def realiza_checkin(self, cliente: str): 
        reserva_encontrada = False
        quarto_encontrado = False

        # Lê as reservas do arquivo
        try:
            with open("reserva.txt", "r") as arquivo:
                reservas = arquivo.readlines()
        except FileNotFoundError:
            print("Arquivo de reservas não encontrado.")
            return

        # Procura pela reserva do cliente
        for i, linha in enumerate(reservas):
            dados = linha.strip().split(',')
            numero_quarto = int(dados[0])
            cliente_reserva = dados[1].strip()
            dia_inicio = dados[2]
            dia_fim = dados[3]
            status = dados[4]

            # Verifica se a reserva é a do cliente e se está ativa
            if cliente_reserva == cliente and status == 'A':
                reserva_encontrada = True

                # Verifica a disponibilidade do quarto
                data_checkin = dia_inicio  # Usaremos a data de início da reserva como data de check-in
                data_checkin_int = int(data_checkin.replace('/', ''))  # Converte a data para formato inteiro

                # Verifica se a reserva está ativa
                if data_checkin_int >= int(dia_inicio.replace('/', '')) and data_checkin_int <= int(dia_fim.replace('/', '')):
                    # Calcula a quantidade de dias reservados
                    dias_reserva = self.calcula_dias(dia_inicio, dia_fim)
                    print(f"Reserva encontrada para o cliente {cliente}:")
                    print(f"Data de início: {dia_inicio}, Data de fim: {dia_fim}, Dias reservados: {dias_reserva}")

                    # Busca o valor da diária do quarto
                    try:
                        with open("quarto.txt", "r") as arquivo_quartos:
                            for linha_quarto in arquivo_quartos:
                                dados_quarto = linha_quarto.strip().split(',')
                                numero_quarto_quarto = int(dados_quarto[0])
                                categoria = dados_quarto[1].strip()
                                valor_diaria = float(dados_quarto[2].strip())

                                if numero_quarto_quarto == numero_quarto:
                                    quarto_encontrado = True
                                    valor_total = dias_reserva * valor_diaria
                                    print(f"Quarto: {numero_quarto_quarto}, Categoria: {categoria}, Valor da diária: R$ {valor_diaria:.2f}")
                                    print(f"Valor total da estadia: R$ {valor_total:.2f}")
                                    break

                    except FileNotFoundError:
                        print("Arquivo de quartos não encontrado.")
                        return

                    # Atualiza o status da reserva para 'I' (Check-In)
                    reservas[i] = f"{numero_quarto},{cliente_reserva},{dia_inicio},{dia_fim},I\n"  # Muda o status

                    # Salva a alteração de status no arquivo
                    with open("reserva.txt", "w") as arquivo:
                        arquivo.writelines(reservas)

                    print("Check-in realizado com sucesso!")
                    return  # Finaliza a função

                else:
                    print(f"O quarto {numero_quarto} não está disponível na data {data_checkin}.")
                break

        if not reserva_encontrada:
            print(f"Não foi encontrada reserva ativa para o cliente {cliente}.")

    
    def calcula_dias(self, dia_inicio: str, dia_fim: str) -> int:
        # Extrai o dia, mês e ano
        dia_i, mes_i, ano_i = map(int, dia_inicio.split('/'))
        dia_f, mes_f, ano_f = map(int, dia_fim.split('/'))

        # Calcula o total de dias
        total_dias_inicio = ano_i * 365 + mes_i * 30 + dia_i  # Aproximando os meses como 30 dias
        total_dias_fim = ano_f * 365 + mes_f * 30 + dia_f  # Aproximando os meses como 30 dias

        return total_dias_fim - total_dias_inicio



    # + realiza_checkout(cliente)
    def realiza_checkout(self, cliente: str):
        reserva_encontrada = False
        consumo_total = 0
        quarto_encontrado = False

        # Lê as reservas do arquivo
        try:
            with open("reserva.txt", "r") as arquivo:
                reservas = arquivo.readlines()
        except FileNotFoundError:
            print("Arquivo de reservas não encontrado.")
            return

        # Procura pela reserva do cliente em check-in
        for i, linha in enumerate(reservas):
            dados = linha.strip().split(',')
            numero_quarto = int(dados[0])
            cliente_reserva = dados[1].strip()
            dia_inicio = dados[2]
            dia_fim = dados[3]
            status = dados[4]

            # Verifica se a reserva é do cliente e está em check-in
            if cliente_reserva == cliente and status == 'I':  # Status 'I' (Check-In)
                reserva_encontrada = True
                dias_reserva = self.calcula_dias(dia_inicio, dia_fim)

                # Calcula valor total das diárias
                try:
                    with open("quarto.txt", "r") as arquivo_quartos:
                        for linha_quarto in arquivo_quartos:
                            dados_quarto = linha_quarto.strip().split(',')
                            numero_quarto_quarto = int(dados_quarto[0])
                            categoria = dados_quarto[1].strip()
                            valor_diaria = float(dados_quarto[2].strip())

                            if numero_quarto_quarto == numero_quarto:
                                quarto_encontrado = True
                                valor_total_diarias = dias_reserva * valor_diaria
                                print(f"Check-out para o cliente {cliente}:")
                                print(f"Data de início: {dia_inicio}, Data de fim: {dia_fim}, Dias reservados: {dias_reserva}")
                                print(f"Quarto: {numero_quarto_quarto}, Categoria: {categoria}, Valor da diária: R$ {valor_diaria:.2f}")
                                print(f"Valor total das diárias: R$ {valor_total_diarias:.2f}")
                                break

                except FileNotFoundError:
                    print("Arquivo de quartos não encontrado.")
                    return

                # Verifica e calcula o consumo do quarto
                try:
                    with open("consumo.txt", "r") as arquivo_consumo:
                        consumos = arquivo_consumo.readlines()

                        consumos_quarto = [c for c in consumos if c.startswith(str(numero_quarto))]
                        if consumos_quarto:
                            print("Consumos registrados:")
                            for consumo in consumos_quarto:
                                dados_consumo = consumo.strip().split(',')
                                if len(dados_consumo) == 3:  # Verifica se a linha de consumo tem exatamente 3 elementos
                                    codigo_produto = dados_consumo[2]  # O código do produto consumido

                                    # Lê o arquivo de produtos para obter os valores
                                    with open("produto.txt", "r") as arquivo_produto:
                                        for linha_produto in arquivo_produto:
                                            dados_produto = linha_produto.strip().split(',')
                                            if dados_produto[0] == codigo_produto:
                                                nome_produto = dados_produto[1]
                                                valor_produto = float(dados_produto[2])
                                                consumo_total += valor_produto
                                                print(f"{nome_produto} - R$ {valor_produto:.2f}")
                                                break  # Encerra a busca assim que encontra o produto
                                else:
                                    print(f"Dados incompletos na linha de consumo: {consumo.strip()}")
                        else:
                            print("Nenhum consumo registrado para este quarto.")
                except FileNotFoundError:
                    print("Arquivo de consumo não encontrado.")
                    return

                # Calcula o valor total a pagar
                valor_final = valor_total_diarias + consumo_total
                print(f"Valor final a ser pago (diárias + consumo): R$ {valor_final:.2f}")

                # Atualiza o status da reserva para 'O' (Check-Out)
                reservas[i] = f"{numero_quarto},{cliente_reserva},{dia_inicio},{dia_fim},O\n"

                # Salva as mudanças no arquivo reserva.txt
                with open("reserva.txt", "w") as arquivo:
                    arquivo.writelines(reservas)

                # Remove os consumos do cliente e do quarto após o check-out
                consumos_remanescentes = [c for c in consumos if not c.startswith(str(numero_quarto))]
                
                # Salva o arquivo consumo.txt com os consumos restantes
                with open("consumo.txt", "w") as arquivo_consumo:
                    arquivo_consumo.writelines(consumos_remanescentes)

                print("Check-out realizado com sucesso.")
                break

        if not reserva_encontrada:
            print(f"Não foi encontrada reserva em check-in para o cliente {cliente}.")




    def registrar_consumo(self):
        cliente = input("Informe o nome do cliente: ")
        numero_quarto = input("Informe o número do quarto: ")
        print()
        # Exibe a lista de produtos disponíveis
        print("\nLista de produtos disponíveis:")
        with open("produto.txt", "r") as arquivo:
            for linha in arquivo:
                codigo, nome, valor = linha.strip().split(',')
                print(f"Código: {codigo}, Nome: {nome}, Valor: R$ {valor}")
        print()
        codigo_produto = input("Informe o código do produto: ")

        # Verifica se existe check-in ativo para o cliente
        checkin_ativo = False
        for reserva in self.__reservas:
            if reserva.cliente == cliente and reserva.status == 'I': 
                checkin_ativo = True
                break

        if not checkin_ativo:
            print("Não há check-in ativo para o cliente informado.")
            return


        # Registra o consumo no arquivo consumo.txt
        with open("consumo.txt", "a") as arquivo_consumo:
            arquivo_consumo.write(f"{numero_quarto},{cliente},{codigo_produto}\n")
        print("Consumo registrado com sucesso.")

    def __str__(self):
        return f"Pousada: {self.__nome}, Contato: {self.__contato}"
    

