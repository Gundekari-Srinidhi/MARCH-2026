class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n=len(mat)
        m=len(mat[0])
        d={}
        d1={}
        for i in range(n):
            for j in range(m):
                if mat[i][j]==1:
                    if i in d:
                        d[i]+=1
                    else:
                        d[i]=1
                    if j in d1:
                        d1[j]+=1
                    else:
                        d1[j]=1
        count=0
        for i in range(n):
            for j in range(m):
                if mat[i][j]==1:
                    if d[i]==1 and d1[j]==1:
                        count+=1
        return count
                

        