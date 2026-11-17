class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            if nums[l] < nums[r]:
                # sorted array
                return nums[l]

            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                # min in right array
                l = mid + 1
            else: r = mid
        return nums[l]
            
            