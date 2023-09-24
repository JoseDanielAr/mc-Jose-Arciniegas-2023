import numpy as np


M1 = np.array([[3,3,1], [2,1,0], [2,-3,-2]])


I = np.identity(3)


M1 = np.concatenate((M1, I), axis=1)

for i in range(3):
 
    M1[i] /= M1[i][i]
    for j in range(3):
        if i != j:
            
            M1[j] -= M1[i] * M1[j][i]

M1 = M1[:, 3:]

print(M1)

M2 = np.array([[1,2,1,0],[2,0,1,4],[0,-1,-1,1],[4,-2,0,0]])

I = np.eye(M2.shape[0])

augmented_matrix = np.concatenate((M2, I), axis=1)

for i in range(augmented_matrix.shape[0]):
    pivot = augmented_matrix[i, i]
    augmented_matrix[i] /= pivot
    for j in range(augmented_matrix.shape[0]):
        if i != j:
            factor = augmented_matrix[j, i]
            augmented_matrix[j] -= factor * augmented_matrix[i]

M2 = augmented_matrix[:, M2.shape[0]:]

print(M2)
