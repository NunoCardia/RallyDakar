import Rally
import Tarefa2
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
    # s = Rally.Tarefa1().read_symbols()
    # print(len(s))
    inicio = process_time()
    # a = Rally.Tarefa1().geradorMapas(10,s)
    # Rally.Tarefa1().print_map(a)
    #m = t.create_adjancency_maxtrix(a)
    s = Tarefa2.Tarefa2().read_symbols()
    a = Tarefa2.Tarefa2().geradorMapas(10, s)
    Tarefa2.Tarefa2().print_map(a)
    m = t.create_adjancency_maxtrix(a)
    t.solve_tsp(m,a)
    fim = process_time()
    print("Operação concluida em " + str(fim - inicio) + " segundos")



    #t.solve_tsp(m)

if __name__ == "__main__":
    main()
