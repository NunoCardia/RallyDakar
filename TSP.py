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


    def solve_tsp(self,matrix,map):#TODO travelling salesman problem: nearest neighbour algorithm -- DONE
        visited = []
        path = []
        temp = []
        cost = 0
        path.append(map[0].symbol)
        next_index = 0
        for i in range(len(matrix)-1):
            for j in matrix[next_index]:
                if j > 0 and matrix[next_index].index(j) not in visited:
                    temp.append(int(j))
            min_lane = min(temp)
            cost += int(min_lane)
            for key,value in map[next_index].connections.items():
                if value == min_lane:
                    path.append(key)
                    break
            visited.append(next_index)
            next_index = matrix[next_index].index(min_lane)
            temp.clear()
        path.append(map[0].symbol)
        cost+=map[next_index].search_in_dict(path[0])

        for elem in path:
            print(elem,end=' ')
        print("\nTotal cost: " + str(cost))


def main():
    t = TSP()
    Rally.Tarefa1().read_symbols()
    a = Rally.Tarefa1().geradorMapas(10)
    m = t.create_adjancency_maxtrix(a)
    # con1 = {'b':20,'c':42,'d':35}
    # s1 = 'a'
    # con2 = {'a':20,'c':30,'d':34}
    # s2 = 'b'
    # con3 = {'a':42,'b':30,'d':12}
    # s3 = 'c'
    # con4 = {'a':35,'b':34,'c':12}
    # s4 = 'd'
    # rally_map = []
    # new1 = Rally.RallyNode(s1,con1)
    # new2 = Rally.RallyNode(s2, con2)
    # new3 = Rally.RallyNode(s3, con3)
    # new4 = Rally.RallyNode(s4, con4)
    # rally_map.append(new1)
    # rally_map.append(new2)
    # rally_map.append(new3)
    # rally_map.append(new4)
    # m = [[0,20,42,35],[20,0,30,34],[42,30,0,12],[35,34,12,0]]
    t.solve_tsp(m,a)



    #t.solve_tsp(m)

if __name__ == "__main__":
    main()
