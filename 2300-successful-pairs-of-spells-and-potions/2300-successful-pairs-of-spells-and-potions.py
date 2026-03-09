class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n=len(potions)
        ls=[]
        for i in spells:
            l=0
            r=n-1
            while l<=r:
                mid=(l+r)//2
                if i*potions[mid]>=success:
                    r=mid-1
                else:
                    l=mid+1
            ls.append(n-l)
        return ls

        