class Solution:
    def binary_search(self, array, target):
        print('in binary search')
        low = 0
        high = len(array)-1
        print(array)
        while low <= high:
            print("low %s" %low)
            mid = low + (high - low)//2
            if array[mid] == target:
                return True
            elif array[mid] < target:
                low = mid+1
            else:
                high = mid-1
        
        return False
    
    def get_col_array(self, matrix, row, col):
        ret = []
        for i in range(0, row+1):
            ret.append(matrix[i][col])
        return ret
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        
        if not matrix:
            return False
        if not target:
            return False
        
        row = len(matrix)-1
        col = len(matrix[0])-1
        while row >= 0 and col >= 0:
            if matrix[row][col] == target or matrix[row][0] == target or matrix[0][col] == target:
                return True
            elif matrix[row][col] < target:
                return False
            elif matrix[row][col] > target:
                if target > matrix[row][0]:
                    if self.binary_search(matrix[row][:col+1], target):
                        return True
                    else:
                        row -=1
                else:
                    row -= 1
                if target > matrix[0][col]:
                    if self.binary_search(self.get_col_array(matrix, row, col), target):
                        return True
                    else:
                        col -= 1
                else:
                    col -= 1
        return False

if __name__ == "__main__":
    matrix = [[1,   4,  7, 11, 15],
            [2,   5,  8, 12, 19],
            [3,   6,  9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]]
    sol = Solution()
    print(sol.searchMatrix(matrix, 5))
