def get_determinant(matrix):
    n = len(matrix)

    if n != len(matrix[0]):
        #matrix not square
        return None

    if n <= 0:
        return None
    elif n == 1:
        return matrix[0][0]
    else:
        det = 0
        targets = matrix[0]
        for t in range(len(targets)):
            #generate submatrix
            submatrix = [[ r[rc] for rc in range(n) if rc != t] for r in matrix[1:]]

            #multiply against determinant of submatrix
            #and add/subtract value to/from determinant
            if t % 2 == 0:
                #positive
                det += (targets[t] * get_determinant(submatrix))
            else:
                #negative
                det -= (targets[t] * get_determinant(submatrix))
        return det
