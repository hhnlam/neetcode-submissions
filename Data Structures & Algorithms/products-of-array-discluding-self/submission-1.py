class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        res = []
        for i in range(len(nums)-1):
            prefix.append(prefix[i]*nums[i])
        
        inverted_nums = nums[::-1]
        for i in range(len(nums)-1):
            suffix.append(suffix[i]*inverted_nums[i])

        suffix = suffix[::-1]
        for i in range(len(prefix)):
            res.append(prefix[i]*suffix[i])
        return res