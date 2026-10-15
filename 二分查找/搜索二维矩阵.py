class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def func(matrix,target):
            n = len(matrix)
            m = len(matrix[0])
            left =  0
            right = n * m - 1
            while left <= right:
                mid = (left + right) // 2
                if matrix[mid // m][mid % m] < target:
                    left = mid + 1
                elif matrix[mid // m][mid % m] == target:
                    return True
                else:
                    right = mid - 1
            return False

        return func(matrix,target)