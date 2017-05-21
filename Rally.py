import copy
import random
import os
import os.path
from TSP import TSP
from time import process_time


import math

class RallyNode():
    def __init__(self,symbol,connections):
        self.symbol = symbol
        self.connections = connections


    def search_in_dict(self,key):
        return self.connections.get(key,-1)

    def print_node(self):
        return "Symbol: " + str(self.symbol) + "\n" + "Connections: "+ str(self.connections)

class Tarefa1():



    def reptead(self,index1,sym,map):
        return map[index1].connections.get(sym,-1)

    def geradorMapas(self,n_cidades,symbols):
        cities = symbols[:n_cidades]
        rally_list = []
        temp_dict = {}
        for k in range(len(cities)):
            s = cities[k]
            for i in range(len(cities)):
                if cities[i] != s:
                    if i < k:
                        temp_dict[cities[i]] = self.reptead(i,s,rally_list)
                    else:
                        temp_dict[cities[i]] = random.randint(50,1000)
            new = RallyNode(s,copy.deepcopy(temp_dict))
            rally_list.append(new)
            temp_dict.clear()

        return rally_list

    def print_map(self,dakar_map):
        print("Starts in " + str(dakar_map[0].symbol)+"\n")
        visited = []
        for i in range(len(dakar_map)):
            for key,value in dakar_map[i].connections.items():
                if key not in visited:
                    print(dakar_map[i].symbol + " ----> " + key + "\t" + str(value))
            visited.append(dakar_map[i].symbol)

    def read_symbols(self):
        symbol_list = []
        with open('./symbols.txt') as f:
            for line in f:
                line = line.strip()
                symbol_list.append(line)
        return symbol_list

    def search_file(self,path):
        if os.path.isfile(path) and os.access(path, os.R_OK):
            print("Ficheiro já existe e é legível")
            return True
        return False

    def save_repeated_file(self,filename,cidades):
        i = 1
        new_name = filename[:-5] + str(cidades) + '('+ str(i) +')'+ ".txt"
        new_path = "./" + new_name
        while self.search_file(new_path):
            i += 1
            new_name = filename[:-5] + str(cidades) + '('+ str(i) +')'+ ".txt"
            new_path = "./" + new_name

        return new_name

    def write_file(self,rally_list,filename):
        f = open(filename, "w")
        for i in range(len(rally_list)):
            for key, value in rally_list[i].connections.items():
                to_file = str(rally_list[i].symbol) + " " + key + " " + str(value) + "\n"
                f.write(to_file)
        f.close()
        print("Dados guardados no ficheiro " + filename)

    def to_file(self,rally_list,n_cidades):
        filename = "tarefa_1_"
        filename += str(n_cidades) + ".txt"
        path = "./" + filename
        if(self.search_file(path) == True):
            option = input("Quer guardar os dados no mesmo ficheiro?(y/n): ")
            if option == 'n':
                final_name = self.save_repeated_file(filename,n_cidades)
                self.write_file(rally_list,final_name)
            elif option == 'y':
                self.write_file(rally_list,filename)
        else:
            self.write_file(rally_list, filename)

    def input_map(self,cidades):
        symbols = self.read_symbols()
        cities = symbols[:cidades]
        rally_list = []
        temp_dict = {}
        print("Simbolos escolhidos: ")
        for i in range(cidades):
            print(cities[i])
        for i in range(len(cities)):
            for j in range(len(cities)):
                if cities[j] != cities[i]:
                    if j < i:
                        temp_dict[cities[j]] = self.reptead(j,cities[i],rally_list)
                    else:
                        temp_dict[cities[j]] = eval(input(cities[i] + "---->" + cities[j] + " : "))
            new = RallyNode(cities[i], copy.deepcopy(temp_dict))
            rally_list.append(new)
            temp_dict.clear()
        return rally_list

    def quadratic_equation(self,a,b,c):
        delta = ((-b)**2) - (4*a*c)
        if delta < 0:
            delta = -delta
        s1 = int((-b-math.sqrt(delta)) / (2*a))
        s2 = int((-b+math.sqrt(delta)) / (2*a))
        if s1 < 0:
            return s2
        elif s2 < 0:
            return s1

    def get_cidades(self,filename):
        with open(filename) as f:
            for i, l in enumerate(f):
                pass
        return i+1

    def get_line_number(self,filename,number):
        with open(filename) as fp:
            for i, line in enumerate(fp):
                if i == number:
                    return line.rstrip('\n')

    def load_map(self,filename):
        rally_list = []
        temp_dict = {}
        file_length = self.get_cidades(filename)
        temp = -file_length
        cidades = self.quadratic_equation(1,-1,temp)
        n = cidades
        inicio = 0
        fim = n - 1
        for i in range(n):
            for j in range(inicio,fim):
                new_line = self.get_line_number(filename,j)
                number = new_line[4] + new_line[5]
                try:
                    number += new_line[6]
                    number += new_line[7]
                    temp_dict[new_line[2]] = int(number)
                except IndexError:
                    temp_dict[new_line[2]] = int(number)
            simbolo = new_line[0]
            new = RallyNode(simbolo, copy.deepcopy(temp_dict))
            rally_list.append(new)
            temp_dict.clear()
            inicio = fim
            fim = inicio + n - 1
        t = TSP()
        m = t.create_adjancency_maxtrix(rally_list)
        t.solve_tsp(m,rally_list)



    def main_tarefa1_2(self):
        s = self.read_symbols()
        n_cidades = eval(input("Número de cidades: "))
        new = self.geradorMapas(n_cidades,s)
        self.print_map(new)
        option = input("Quer guardar o mapa num ficheiro?(y/n): ")
        if option == 'y':
            self.to_file(new,len(new))

    def main_tarefa1_3(self):
        option = input("Quer carregar um ficheiro?(y/n): ")
        if option == 'y':
            filename = input("Nome do ficheiro: ")
            while not self.search_file("./"+filename):
                filename = input("Ficheiro não existe por favor introduza um nome válido: ")
            inicio = process_time()
            self.load_map(filename)
            fim = process_time()
            print("Operação concluida em " + str(fim - inicio) + " segundos")
        elif option == 'n':
            n_cidades = eval(input("Número de cidades: "))
            rally_list = self.input_map(n_cidades)
            self.print_map(rally_list)
            print("Map created\n\n")
            t = TSP()
            m = t.create_adjancency_maxtrix(rally_list)
            t.solve_tsp(m, rally_list)




