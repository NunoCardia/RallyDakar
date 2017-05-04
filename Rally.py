import string
import copy
import random
import re

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
 #mandar para aqui o rally_list e procurar pela ligação aqui
            if str(key) == cities[i].symbol or str(element) == cities[i].symbol:
                if cities[i].search_in_dict(element) == "Nao existe":
                    return 0
                else:
                    return 1
        return 0


    def geradorMapas(self,n_cidades):
        #gerar todos os simbolos necessarios
        #symbols = list(string.ascii_letters)
        symbols = self.read_symbols()
        #max_dist = eval(input("Distância máxima entre cidades: "))
        #random.shuffle(symbols)
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
                        if self.find_duplicates(rally_list,cities[i],cities[j]) == 0:
                                temp_dict[cities[j]] = random.randint(0,1000)

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
        for i in range(len(dakar_map)):
            for key,value in dakar_map[i].connections.items():
                print(dakar_map[i].symbol + " ----> " + key + "\t" + str(value))

    def read_symbols(self):
        symbol_list = []
        with open('/Users/cyberfox21/Documents/UC/AED/2017/RallyGenerator/symbols.txt') as f:
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
    new = Tarefa1().geradorMapas(7)
    Tarefa1().print_map(new)


if __name__ == "__main__":
    main()

