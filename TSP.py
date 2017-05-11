import Rally
from time import process_time

class TSP():

    def create_adjancency_maxtrix(self,map):
        map_length = len(map)
        adjacency_matrix = [y for y in range(map_length)]
        for i in range(map_length):
            val = [value for value in map[i].connections.values()]
            val.insert(i,0)
            adjacency_matrix[i] = val

        return adjacency_matrix


    def solve_tsp(self,matrix,map):
        path = []
        cost = 0
        path.append(map[0].symbol)
        current = []
        j=0
        for i in range(len(matrix)-1):
            try:
                min_lane = min(k for k in matrix[j] if k > 0 and matrix[j].index(k) not in current)
            except ValueError:
                break
            cost += int(min_lane)
            current.append(j)
            index = matrix[j].index(min_lane)
            path.append(map[index].symbol)
            j = index
        path.append(path[0])
        cost+=map[j].search_in_dict(path[0])


        for elem in path:
            print(elem,end=' ')
        print("\nTotal cost: " + str(cost))


def main():
    t = TSP()
    s = Rally.Tarefa1().read_symbols()
    print(len(s))
    inicio = process_time()
    #a = Rally.Tarefa1().geradorMapas(7,s)
    #m = t.create_adjancency_maxtrix(a)
    con1 = {'b':229,'l':683,'t':769}
    s1 = 'e'
    con2 = {'e':156,'l':954,'t':155}
    s2 = 'b'
    con3 = {'e':439,'b':473,'t':822}
    s3 = 'l'
    con4 = {'e':668,'b':242,'l':378}
    s4 = 't'
    rally_map = []
    new1 = Rally.RallyNode(s1,con1)
    new2 = Rally.RallyNode(s2, con2)
    new3 = Rally.RallyNode(s3, con3)
    new4 = Rally.RallyNode(s4, con4)
    rally_map.append(new1)
    rally_map.append(new2)
    rally_map.append(new3)
    rally_map.append(new4)
    m = [[0,229,683,769],[156,0,954,155],[439,473,0,822],[668,242,378,0]]
    t.solve_tsp(m,rally_map)
    fim = process_time()
    print("Operação concluida em " + str(fim - inicio) + " segundos")



    #t.solve_tsp(m)

if __name__ == "__main__":
    main()
