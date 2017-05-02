import string
import copy
import random

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
                temp_dict[cities[i]] = 10

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
        symbols = list(string.ascii_letters)
        #max_dist = eval(input("Distância máxima entre cidades: "))
        cities = symbols[:n_cidades]
        edges = (n_cidades*(n_cidades - 1))/2
        rally_list = []
        temp_dict = {}
        for i in range(n_cidades):
            #create connections
            #criar o no e as ligações a cada um dos nós
            #A,{B:10 , C:20, D:40}
            for j in range(n_cidades):
                if not rally_list:
                    temp_dict = self.add_empty(n_cidades,cities,cities[i])
                    break
                if cities[i] != cities[j]:
                        if self.find_duplicates(rally_list,cities[i],cities[j]) == 0:
                                temp_dict[cities[j]] = 10


            #print("For city: "+cities[i])
            #for k in temp_dict:
            #    print(k, temp_dict[k])
            new = RallyNode(cities[i],copy.deepcopy(temp_dict),1)
            rally_list.append(new)
            temp_dict.clear()

        for k in range(len(rally_list)):
            print(rally_list[k].print_node(),sep='\n')

        sum = 0
        for elem in rally_list:
            sum += len(elem.connections)

        if sum == edges:
            print("This is a complete graph by definition")




def main():
    #dict = {"B":30 , "C":40}
    #new = RallyNode("A",dict)
    #final = new.search_in_dict(dict,"B")
    #print("Found: " + str(final))
    new = Tarefa1().geradorMapas(7)

if __name__ == "__main__":
    main()

