class Solution:
    def uniquePaths(self, r: int, c: int) -> int:
        dp=[[-1]*(c+1) for i in range(r+1)] 
        def grid(r,c):
            if r==1 or c==1:
                return 1
            if dp[r][c]!=-1:
                return dp[r][c]
            dp[r][c]=grid(r-1,c)+grid(r,c-1)
        
            return dp[r][c]
        return grid(r,c)