import os
from TSP import TSP
import Rally
from Tarefa2 import Tarefa2
from time import process_time

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
        Tarefa2().main_tarefa2_2()
    elif option1 == 2:
        Tarefa2().main_tarefa2_3()
    elif option1 == 3:
        os.system('clear')
        return 0

def main():
    main_menu()



if __name__ == "__main__":
    t = TSP()
    s = Rally.Tarefa1().read_symbols()

    inicio = process_time()
    a = Rally.Tarefa1().geradorMapas(22510, s)
    m = t.create_adjancency_maxtrix(a)
    t.solve_tsp(m, a)
    fim = process_time()
    print("Operação 25500 concluida em " + str(fim - inicio) + " segundos")
    inicio = process_time()
    a = Rally.Tarefa1().geradorMapas(22520, s)
    m = t.create_adjancency_maxtrix(a)
    t.solve_tsp(m, a)
    fim = process_time()
    print("Operação 25550 concluida em " + str(fim - inicio) + " segundos")
    inicio = process_time()
    a = Rally.Tarefa1().geradorMapas(22540, s)
    m = t.create_adjancency_maxtrix(a)
    t.solve_tsp(m, a)
    fim = process_time()
    print("Operação 25555 concluida em " + str(fim - inicio) + " segundos")

