def matrix(r, c, mat):
    return r, c, mat

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

print("Enter the matrix row by row (space-separated):")
mat = []
for i in range(rows):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    if len(row) != columns:
        print(f"Please enter exactly {columns} elements.")
        exit()
    mat.append(row)

result = matrix(rows, columns, mat)
print("Output:")
print(result)

def set_matrix_zeros(r,c,mat):
    zero_rows = set()
    zero_cols = set()
    
    for i in range(r):
        for j in range(c):
            if mat[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)
    
    for i in range(r):
        for j in range(c):
            if i in zero_rows or j in zero_cols:
                mat[i][j] = 0
    return mat
    
# print(set_matrix_zeros(rows, columns, mat))
result = set_matrix_zeros(rows, columns, mat)
for row in result:
    print(row)