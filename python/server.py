matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
strok = len(matrix)
M = len(matrix[0]) 


qwet = [[0] * strok for _ in range(M)] 
for j in range(M):
    for i in range(strok):  
        qwet[j][i] = matrix[strok - 1 - i][j]


print()
for w in qwet:
    print(w)


print("wert"7)