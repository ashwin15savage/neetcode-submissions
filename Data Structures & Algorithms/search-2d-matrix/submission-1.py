class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS=len(matrix)
        COLS=len(matrix[0])

        topRow=0
        botRow=ROWS-1

        while topRow<=botRow:

            midRow=(topRow+botRow)//2

            if target>matrix[midRow][-1]:
                topRow=midRow+1
            elif target<matrix[midRow][0]:
                botRow=midRow-1
            else:
                break
        if not (topRow<=botRow):
            return False
        
        l=0
        r=COLS-1

        row=(topRow+botRow)//2

        while l<=r:
            m=(l+r)//2

            if target>matrix[row][m]:
                l=m+1
            elif target<matrix[row][m]:
                r=m-1
            else:
                return True
        return False
            


        
                    