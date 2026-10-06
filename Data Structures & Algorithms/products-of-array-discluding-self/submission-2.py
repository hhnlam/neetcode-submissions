class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        prefix[0] = suffix[n-1] = 1
        res = [0] * n

        for i in range(n-1):
            prefix[i+1] = prefix[i] * nums[i]
        
        for i in range(n-1, 0, -1):
            suffix[i-1] = suffix[i] * nums[i]
        
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        return res