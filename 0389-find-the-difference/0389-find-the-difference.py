class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        l=list(s)
        n=len(t)
        for i in range(n):
            if t[i] not in l:
                return t[i]
            else:
                l.remove(t[i])
            
            
        