class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        d={}
        l=0
        r=0
        pairs=0
        n=len(nums)
        count=0
        for r in range(n):
            if nums[r] in d:
                pairs+=d[nums[r]]
                d[nums[r]]+=1
            else:
                d[nums[r]]=1
            while pairs>=k:
                count+=len(nums)-r
                d[nums[l]]-=1
                pairs-=d[nums[l]]
                l+=1
        return count





        