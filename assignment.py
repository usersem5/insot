
def reduce_rows(matrix):
    # Subtract the minimum value of each row from all elements of that row
    for i in range(len(matrix)):
        min_value = min(matrix[i])
        matrix[i] = [x - min_value for x in matrix[i]]
    return matrix

def reduce_columns(matrix):
    # Subtract the minimum value of each column from all elements of that column
    num_columns = len(matrix[0])
    for j in range(num_columns):
        # Find the minimum value in the column
        min_value = min(matrix[i][j] for i in range(len(matrix)))
        # Subtract the minimum value from each element in the column
        for i in range(len(matrix)):
            matrix[i][j] -= min_value
    return matrix

# Define a 5x5 cost matrix
cost_matrix = [
    [9, 2, 7, 8, 5],
    [6, 4, 3, 7, 3],
    [5, 8, 1, 8, 4],
    [7, 6, 9, 5, 6],
    [6, 3, 4, 5, 9]
]

print("Original cost matrix:")
for row in cost_matrix:
    print(row)

# Step 1: Subtract the smallest element of each row
reduced_matrix = reduce_rows([row[:] for row in cost_matrix])
print("Matrix after row reduction:")
for row in reduced_matrix:
    print(row)

# Step 2: Subtract the smallest element of each column
reduced_matrix = reduce_columns(reduced_matrix)
print("Matrix after column reduction:")
for row in reduced_matrix:
    print(row)
    
