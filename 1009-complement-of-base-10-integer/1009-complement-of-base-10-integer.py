class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n==0:
            return 1
        s=""
        while n>0:
            if n%2==0:
                s+="1"
            else:
                s+="0"
            n=n//2
        if n%2!=0:
            s=s[::-1]
        val=0
        for i in range(len(s)):
            if s[i]=="1":
                val+=2**i
        return val


        