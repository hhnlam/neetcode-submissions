class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff not in seen:
                seen[num] = i
            else:
                return [seen[diff], i]