M1 = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

M2 = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = []

M1_size_row = len(M1)
M1_size_col = len(M1[0])
M2_size_row = len(M2)
M2_size_col = len(M2[0])


if M1_size_col > M2_size_col:
    total_col = M1_size_col
else:
    total_col = M2_size_col

if M1_size_row > M2_size_row:
    total_row = M1_size_row
else:
    total_row = M2_size_row

for i in range(total_row):
    row = []
    for j in range(total_col):
        row.append(0)
    result.append(row)

def MatrixAddition(a,b):
    if M1_size_col == M2_size_col and M1_size_row == M2_size_row:
        for i in range(len(a)):
            for j in range(len(a[0])):
                    result[i][j] = a[i][j] + b[i][j]
        return result
    else:
        print("Error : Dimension of matrix M1 and M2 are not equal")

def MatrixTranspose(a):
    if M1_size_col == M2_size_col and M1_size_row == M2_size_row:
        for i in range(len(a)):
            for j in range(len(a[0])):
                result[j][i] = a[i][j]
        return result
    else:
        print("Error : Dimension of matrix M1 and M2 are not equal")

def MatrixMultiplication(a,b):
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

def MatrixMinor(a,i,j):
    c = a
    c = c[:i] + c[i+1:]
    for k in range(0,len(c)):
        c[k] = c[k][:j]+c[k][j+1:]
    return c

def MatrixDeternminant(a,n):
    if M1_size_col == M2_size_col and M1_size_row == M2_size_row:
        if n == 1 :return a[0][0]
        if n == 2 :return a[0][0]*a[1][1] - a[0][1]*a[1][0]
        sum = 0
        for i in range(0,n):
            m = MatrixMinor(a,0,i)
            sum =sum + ((-1)**i)*a[0][i] * MatrixDeternminant(m,n-1)
        return sum
    else:
        print("Error : Dimension of matrix is not square")


print(MatrixAddition(M1,M2))
print(MatrixTranspose(M1))
print(MatrixMultiplication(M1,M2))
print(MatrixDeternminant(M1,3))
