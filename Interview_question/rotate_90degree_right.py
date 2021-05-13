def rotate_array_right(array):
    for i in range(len(array)):
        j = len(array) - 1
        while j >= 0:
            print(array[j][i]," " , end="")
            j -= 1
        print("", end = "\n")

print(rotate_array_right([[1,2,3], [4,5,6],[7,8,9]]))
