class Solution(object):
    def searchMatrix(self, matrix, target):
        
        rows=len(matrix)
        columns=len(matrix[0])
        j=columns-1
        i=0
        while i<rows and j>=0:
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]<target:
                i+=1
            elif matrix[i][j]>target:
                j-=1
        return False
