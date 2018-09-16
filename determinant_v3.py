#fixed non-square matrix check

def det(matrix):
    if check_square(matrix) == False:
        print ("this is not a square matrix >:(")
        return None
    else:
        if len(matrix) == 1:
            return matrix[0]
        elif len(matrix) == 2:
            return (matrix[0][0])*(matrix[1][1])-(matrix[0][1])*(matrix[1][0])
        else:
            total = 0
            for i in range(0,len(matrix)):
                total = total + ((-1)**i)*matrix[0][i]*det(shrink(matrix,i))
            return total

def shrink(matrix,k):
    matrix_copy=copy(matrix)
    matrix_copy.remove(matrix_copy[0])
    for i in range(0,len(matrix_copy)):
        matrix_copy[i].pop(k)
    return matrix_copy

def copy(matrix):
    matrix_copy=[]
    for i in range(0,len(matrix)):
        tiny_copy=[]
        for j in range(0,len(matrix[i])):
            tiny_copy.append(matrix[i][j])
        matrix_copy.append(tiny_copy)
    return matrix_copy

def check_square(matrix):
    for i in matrix:
        if len(i) != len(matrix):
            return False
        return True