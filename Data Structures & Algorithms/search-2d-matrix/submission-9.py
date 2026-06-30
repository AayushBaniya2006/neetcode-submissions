class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, r = 0, len(matrix) - 1
        mid = 0 

        while l <= r:
            mid = int((l + r)/2)

            if(target > matrix[mid][-1]):
                l = mid + 1
            elif(target < matrix[mid][0]):
                r = mid - 1
            else: 
                break

        if not (l <= r):
            return False

        print(matrix[mid])

        l, r = 0, len(matrix[0]) - 1
        m = 0

        while l <= r: 
            m = (l + r) // 2

            if(target < matrix[mid][m]):
                r = m - 1
            elif(target > matrix[mid][m]):
                l = m + 1
            else: 
                return True           

        return False