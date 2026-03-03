class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def convert(val):
            st=""
            for i in val:
                if i=="1":
                    st+="0"
                else:
                    st+="1"
            return st[::-1]
        def find(n,s):
            if n==0:
                return "0"
            val=find(n-1,s)
            s+=val+"1"+convert(val)
            return s
        s=""
        ans=find(n,s)
        return ans[k-1]
        