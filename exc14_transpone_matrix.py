mat1 = input('Put in the numbers for the first matrix, separating them with comas: ')
mat1 = mat1.split(',')
matrix1 = [[int(mat1[0]), int(mat1[1]), int(mat1[2])],
           [int(mat1[3]), int(mat1[4]), int(mat1[5])],
           [int(mat1[6]), int(mat1[7]), int(mat1[8])]]
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[j][i]
print(f'''Your original matrix: 
[[{int(mat1[0])}, {int(mat1[1])}, {int(mat1[2])}],
[{int(mat1[3])}, {int(mat1[4])}, {int(mat1[5])}],
[{int(mat1[6])}, {int(mat1[7])}, {int(mat1[8])}]]
Your transponed matrix:''')
for i in result:
    print(i)
