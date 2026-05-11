class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = rows*cols - 1

        while l<=r :
            mid = (l+r)//2

            newRow = mid//cols
            newCol = mid%cols

            number = matrix[newRow][newCol]

            if target == number:
                return True
            elif target<number:
                r = mid-1
            else:
                l = mid+1

        return False
            



        




        