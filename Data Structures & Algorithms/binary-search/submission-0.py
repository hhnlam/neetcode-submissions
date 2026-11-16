class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            search = (right + left) // 2
            
            if nums[search] == target: return search
            elif nums[search] > target: right = search - 1
            elif nums[search] < target: left = search + 1
        return -1