class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        ROWS=len(matrix)
        COLS=len(matrix[0])

        cache={} #map each (r,c) to max area len


        def helper(r,c):

            if r>=ROWS or c>=COLS:
                return 0
            
            if (r,c) not in cache:

                cache[(r,c)]=0

                down=helper(r+1,c)
                right=helper(r,c+1)
                diag=helper(r+1,c+1)

                if matrix[r][c]=="1":
                    cache[(r,c)]=1+min(down,right,diag)

            return cache[(r,c)]

        helper(0,0)

        maxSqlen=max(cache.values())
        return maxSqlen**2
        