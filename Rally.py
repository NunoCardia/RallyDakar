import string
import copy
import random
import re
import sys

class RallyNode():
    def __init__(self,symbol,connections,check=0):
        self.symbol = symbol
        self.connections = connections


    def search_in_dict(self,key):
        return self.connections.get(key,"Nao existe") #procura no dicionario se a key existe e retorna o elemento, caso n tenha retorna o segundo parametro

    def print_node(self):
        return "Symbol: " + str(self.symbol) + "\n" + "Connections: "+ str(self.connections)

class Tarefa1():

    def add_empty(self,n_cidades,cities,city):
        temp_dict = {}
        for i in range(n_cidades):
            if city != cities[i]:
                temp_dict[cities[i]] = random.randint(0,1000)

        return temp_dict

    def find_duplicates(self,cities,element,key):
        for i in range(len(cities)):
            if str(key) == cities[i].symbol or str(element) == cities[i].symbol:
                answer =cities[i].search_in_dict(element)
                if  answer == "Nao existe":
                    return 0
                else:
                    return answer
        return 0


    def geradorMapas(self,n_cidades):
        #symbols = self.read_symbols()
        symbols = string.ascii_letters
        cities = symbols[:n_cidades]
        edges = (n_cidades*(n_cidades - 1))/2
        rally_list = []
        temp_dict = {}
        for i in range(n_cidades):
            for j in range(n_cidades):
                if not rally_list:
                    temp_dict = self.add_empty(n_cidades,cities,cities[i])
                    break
                if cities[i] != cities[j]:
                    answer = self.find_duplicates(rally_list,cities[i],cities[j])
                    if answer == 0:
                            temp_dict[cities[j]] = random.randint(0,1000)
                    else:
                        temp_dict[cities[j]] = answer

            new = RallyNode(cities[i],copy.deepcopy(temp_dict),1)
            rally_list.append(new)
            temp_dict.clear()

        sum = 0
        for elem in rally_list:
            sum += len(elem.connections)

        if sum == edges:
            print("This is a complete graph by definition")

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
        with open('symbols.txt') as f:
            for line in f:
                line = line.strip()
                symbol_list.append(line)
        return symbol_list






def main():
    #dict = {"B":30 , "C":40}
    #new = RallyNode("A",dict)
    #final = new.search_in_dict(dict,"B")
    #print("Found: " + str(final))
    Tarefa1().read_symbols()
    new = Tarefa1().geradorMapas(4)
    Tarefa1().print_map(new)
    #Tarefa1().dij()
    distances = {
        'B': {'A': 20, 'D': 34, 'C': 30},
        'A': {'B': 20, 'D': 35, 'C': 42},
        'D': {'A': 35, 'B': 34, 'C': 12},
        'C': {'A': 42, 'B': 30, 'D': 12}}



if __name__ == "__main__":
    main()

