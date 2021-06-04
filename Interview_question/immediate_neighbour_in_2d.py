def immediate_neighbour_in_2darray(array, num):
    neighbours = []
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][j] == num:
                if j - 1 >= 0:
                    neighbours.append((array[i][j], array[i][j - 1]))
                if j + 1 <= len(array) - 1:
                    neighbours.append((array[i][j], array[i][j + 1]))
                if i - 1 >= 0:
                    neighbours.append((array[i][j], array[i-1][j]))
                if i + 1 <= len(array) - 1:
                    neighbours.append((array[i][j], array[i+1][j]))
    return neighbours
array = [[1,2,3],[4,5,6],[7,8,9]]
print(immediate_neighbour_in_2darray(array, 5))