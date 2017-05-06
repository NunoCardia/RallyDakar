import Rally

class TSP():

    def create_adjancency_maxtrix(self,map):
        map_length = len(map)
        adjacency_matrix = [[0 for x in range(map_length)] for y in range(map_length)]
        for i in range(map_length):
            val = [value for value in map[i].connections.values()]
            val.insert(i,0)
            for j in range(map_length):
                if j == i:
                    adjacency_matrix[i][j] = 0
                else:
                    adjacency_matrix[i][j] =  val[j]
        return adjacency_matrix


    def solve_tsp(self,matrix):
        pass


def main():
    n = eval(input("Number of symbols: "))
    t = TSP()
    Rally.Tarefa1().read_symbols()
    a = Rally.Tarefa1().geradorMapas(4)
    t.create_adjancency_maxtrix(a)



    #t.solve_tsp(m)

if __name__ == "__main__":
    main()
