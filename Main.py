import sys
import time
from Classes import Reserva
from Classes import Quarto

f = open('reserva.txt', 'r')
g = open('pousada.txt', 'r')
h = open('produto.txt', 'r')
i = open('quarto.txt', 'r')

def main():
    print()
    print("|----------------------------------------------|")
    print("|                                              | ") 
    print("|             O que você deseja?               | ") 
    print("|                                              | ") 
    print("|    1) Consultar disponibilide                | ")              
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
    print()
    escolha = int(input("Digite aqui a opção que você deseja: "))
    
    if escolha == 1:
        print("Consultar disponibilidade")

    elif escolha == 2:
        print("Consultar reserva")

    elif escolha == 3:
        print("Realizar reserva")

    elif escolha == 4:
        print("Cancelar reserva")

    elif escolha == 5:
        print("Realizar check-in")

    elif escolha == 6:
        print("Realizar check-out")

    elif escolha == 7:
        print("Registrar consumo")

    elif escolha == 8:
        print("Salvar")

    elif escolha == 0:
        print("Encerrando o programa...")
        time.sleep(2)
        sys.exit

    else:
        print("Digite um número entre 0-8 para a opção desejada")

main()
