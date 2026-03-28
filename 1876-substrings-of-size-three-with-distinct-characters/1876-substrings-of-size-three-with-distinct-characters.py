class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        l = 0
        r = 3
        while r <= n:
            val = set(s[l:r])
            if len(val) == 3:
                count+=1
            l+=1
            r+=1
        return count
        