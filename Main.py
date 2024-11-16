#DIEGO ELLWANGER & JOÃO VITOR DALCIN ANDRIOLI

import sys
import time
from Classes.Reserva import Reserva
from Classes.Quarto import Quarto
from Classes.Pousada import Pousada
from Classes.Produto import Produto




def main():
    # Inicializa a pousada com nome e contato
    pousada = Pousada("Pousada Recanto", "contato@recanto.com")

    #CARREGA OS DADOS DOS ARQUIVOS
    pousada.carrega_dados()
    
    
    while True:
        print()
        print("|----------------------------------------------|")
        print("|                                              |") 
        print("|             O que você deseja?               |") 
        print("|                                              |") 
        print("|    1) Consultar disponibilidade              |")              
        print("|    2) Consultar reserva                      |")
        print("|    3) Realizar reserva                       |")
        print("|    4) Cancelar reserva                       |")
        print("|    5) Realizar check-in                      |")
        print("|    6) Realizar check-out                     |")
        print("|    7) Registrar consumo                      |")
        print("|    8) Salvar                                 |")
        print("|    0) Sair                                   |")
        print("|                                              |")
        print("|----------------------------------------------|")
        print()
        escolha = int(input("Digite aqui a opção que você deseja: "))
        
        if escolha == 1:
            print("Consultar disponibilidade")
            data = input("Informe a data (dd/mm/aaaa): ")
            numero_quarto = int(input("Informe o número do quarto: "))
            # Aqui você pode consultar se o quarto está disponível na data

            # Chama a função consultar_disponibilidade da classe Pousada
            pousada.consulta_disponibilidade(data, numero_quarto)
            
            
        
        elif escolha == 2:
            print("Consultar reserva")
            data = input("Informe a data da reserva (dd/mm/aaaa): ")
            cliente = input("Informe o nome do cliente: ")
            numero_quarto = int(input("Informe o número do quarto: "))
            
            
            reserva = pousada.consulta_reserva(data, cliente, numero_quarto)

            if reserva:
                print(f"Sua reserva está tudo OK para a data {data}, no quarto {numero_quarto}.")
            else:
                print(f"Não foi possível localizar reserva para a data {data}, no quarto {numero_quarto}.")
            time.sleep(2)

        elif escolha == 3:
            print("Realizar reserva")

            # Coletando informações da reserva
            data_inicio_str = input("Digite o dia de início da reserva (dd/mm/aaaa): ")
            data_fim_str = input("Digite o dia de fim da reserva (dd/mm/aaaa): ")
            cliente = input("Informe o nome do cliente: ")
            numero_quarto = int(input("Informe o número do quarto: "))
            
            # Chamar o método realiza_reserva para adicionar a reserva no arquivo
            pousada.realiza_reserva(data_inicio_str, data_fim_str, cliente, numero_quarto)

        elif escolha == 4:
            print("Cancelar reserva")
            cliente = input("Informe o nome do cliente: ")
            pousada.cancela_reserva(cliente)
            time.sleep(2)

        elif escolha == 5:
            print("Realizar check-in")
            cliente = input("Informe o nome do cliente: ")
            pousada.realiza_checkin(cliente)
            time.sleep(6)

        elif escolha == 6:
            print("Realizar check-out")
            cliente = input("Informe o nome do cliente: ")
            print()
            pousada.realiza_checkout(cliente)
            time.sleep(6)

        elif escolha == 7:
            print("Registrar consumo")
            

            # Chama a função registrar_consumo da classe Pousada
            pousada.registrar_consumo() 
            time.sleep(2)

        elif escolha == 8:
            print("Salvar dados")
            pousada.salva_dados()

        elif escolha == 0:
            pousada.salva_dados()
            print("Encerrando o programa...")
            time.sleep(2)
            sys.exit()

        else:
            print("Digite um número entre 0-8 para a opção desejada")

if __name__ == "__main__":
    main()