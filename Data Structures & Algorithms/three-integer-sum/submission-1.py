class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            # skip duplicate first number
            if i > 0 and num == nums[i-1]: continue

            target = -num

            left = i + 1
            right = len(nums) - 1
            while left < right:
                summation = nums[left] + nums[right]
                if summation > target: right -= 1
                elif summation < target: left += 1
                else: 
                    res.append([num, nums[left], nums[right]])
                    while left<right and nums[left+1] == nums[left]: left+=1
                    while left<right and nums[right-1] == nums[right]: right-=1
                    left += 1
                    right -= 1
        return res
