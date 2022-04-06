class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        mid = (right + left) // 2
        while left < right:
            if matrix[mid][-1] < target:
                left = mid + 1
            elif matrix[mid][0] > target:
                right = mid
            else:
                break
            mid = (right + left) // 2

        if matrix[mid][0] > target or matrix[mid][-1] < target:
            return False

        row = mid
        left = 0
        right = len(matrix[0]) - 1
        mid = (right + left) // 2
        while left < right:
            if matrix[row][mid] < target:
                left = mid + 1
            elif matrix[row][mid] > target:
                right = mid
            else:
                break
            mid = (right + left) // 2

        if matrix[row][mid] == target:
            return True
        else:
            return False


print(Solution.searchMatrix(Solution, [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(Solution.searchMatrix(Solution, [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
print(Solution.searchMatrix(Solution, [[1,3]], 3))
