class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = float('-inf')
        left = 0
        right = len(heights) - 1
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height
            if area > res: res = area
            if heights[left] == height: left += 1
            else: right -= 1
        return res
