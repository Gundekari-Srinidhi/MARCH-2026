class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        count=0
        val="1"
        for i in range(n):
            if s[i]==val:
                count+=1
                if val=="1":
                    s.replace(s[i],"0")
                    val="0"
                else:
                    s.replace(s[i],"1")
                    val="1"
            else:
                val=s[i]
        val1="0"
        count1=0
        for i in range(n):
            if s[i]==val1:
                count1+=1
                if val1=="1":
                    s.replace(s[i],"0")
                    val1="0"
                else:
                    s.replace(s[i],"1")
                    val1="1"
            else:
                val1=s[i]
        return min(count,count1)
        