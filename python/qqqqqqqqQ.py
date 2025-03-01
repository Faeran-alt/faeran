from random import randint
A = []  
N = 4
for i in range(N):
    A.append([randint(10, 99) for j in range(N)]) 



print("исходник:")
for qwer in A:
    for x in qwer:
        print(x, end=" ")
    print()
for i in range(N):
    for j in range(i + 1, N):
        A[i][j] = 0

print("после:")
for qwer in A:
    for x in qwer:
        print(x, end=" ")
    print()