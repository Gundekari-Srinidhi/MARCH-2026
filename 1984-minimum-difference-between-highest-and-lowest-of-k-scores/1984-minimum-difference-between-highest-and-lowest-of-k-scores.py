class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        min_val = float("inf")
        l = 0
        r = k
        while r <= n:
            val = nums[l:r]
            diff = val[-1]-val[0]
            if min_val > diff:
                min_val = diff
            l+=1
            r+=1
        if min_val == float("inf"):
            return 0
        return min_val