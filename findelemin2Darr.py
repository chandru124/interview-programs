class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        columns=len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == target:
                    return True
                else:
                    continue
