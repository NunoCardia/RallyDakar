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
