class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # matrix[n][0] takes rowchange role
        # matrix[0][n] takes colchange role
        rowchecked = False
        colchecked = False
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0: rowchecked = True
                    if j == 0: colchecked = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if rowchecked:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if colchecked:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        
#         rowchange = [0] * len(matrix)     
#         colchange = [0] * len(matrix[0])  
        
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if matrix[i][j] == 0:
#                     rowchange[i] = 1
#                     colchange[j] = 1
        
#         for i, row in enumerate(rowchange):
#             if row == 1:
#                 for j in range(len(matrix[0])):
#                     matrix[i][j] = 0
#         for j, col in enumerate(colchange):
#             if col == 1:
#                 for i in range(len(matrix)):
#                     matrix[i][j] = 0
        
        
