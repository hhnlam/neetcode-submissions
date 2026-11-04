class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix, suffix = [0]*n, [0]*n
        res = 0

        for i in range(1, n):
            prefix[i] = max(height[i-1], prefix[i-1])

        for i in range(n-2, -1, -1):
            suffix[i] = max(height[i+1], suffix[i+1])

        for i in range(1,n):
            area = max(0, min(prefix[i], suffix[i]) - height[i])
            res += area
        return res