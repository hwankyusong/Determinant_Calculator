# input row by row
# thanks to Christian Broms for row by row input idea
# fixed error where shrink function removes wrong element of row

def main():
    k = input("enter first row of matrix \n")
    first = [int(n) for n in k.split(',')]
    i = 0
    matrix=[]
    matrix.append(first)

    while i in range(0,len(first)-1):
        j = input("enter next row of matrix \n")
        l = [int(n) for n in j.split(',')]
        if len(l) != len(matrix[i-1]):
            print("This is not a square matrix")
            return None
        matrix.append(l)
        i = i + 1
    
    print(matrix)
    a = input("Is this your matrix (Y/N)? \n")
    if a == 'Y' or a=='y':
        print("awesome! The determinant of your matrix is:" + str(det(matrix)))
        return None
    else:
        b = input("I'm sorry about that :( \n Try again (Y/N)? \n")
        if b == 'Y':
            return main()
        else:
            print("Okay, bye")
            return None

def det(matrix):
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

if __name__ == "__main__":
    main()