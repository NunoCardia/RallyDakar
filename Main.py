import os
import Rally

def main_menu():
    while True:
        option = eval(input("Projeto 2 de AED\n1 - Tarefa 1\n2 - Tarefa 2\n3 - Sair\n"))
        os.system('clear')
        if option == 1:
            menu_tarefa1()

def menu_tarefa1():
    option1 = eval(input("1 - Gerador automático de mapas\n2 - Caminho mais curto de um mapa\n3 - Voltar\n"))
    if option1 == 1:
        Rally.Tarefa1().main_tarefa1_2()
    elif option1 == 2:
        Rally.Tarefa1().main_tarefa1_3()
    elif option1 == 3:
        os.system('clear')
        return 0

def menu_tarefa2():
    option1 = eval(input("1 - Gerador automático de mapas\n2 - Caminho mais curto de um mapa\n3 - Voltar\n"))
    if option1 == 1:
        Rally.Tarefa2().main_tarefa2_2()
    elif option1 == 2:
        Rally.Tarefa2().main_tarefa2_3()
    elif option1 == 3:
        os.system('clear')
        return 0

def main():
    main_menu()



if __name__ == "__main__":
    main()
