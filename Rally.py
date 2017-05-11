import string
import copy
import random

class RallyNode():
    def __init__(self,symbol,connections,check=0):
        self.symbol = symbol
        self.connections = connections


    def search_in_dict(self,key):
        return self.connections.get(key,-1) #procura no dicionario se a key existe e retorna o elemento, caso n tenha retorna o segundo parametro

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
                        temp_dict[cities[i]] = random.randint(10,1000)
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
        with open('symbols.txt') as f:
            for line in f:
                line = line.strip()
                symbol_list.append(line)
        return symbol_list






def main():
    s = Tarefa1().read_symbols()
    new = Tarefa1().geradorMapas(1000,s)
    Tarefa1().print_map(new)



if __name__ == "__main__":
    main()

