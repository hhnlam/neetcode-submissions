class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        bucket = [[] for i in range(len(nums))]

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        for num, count in counts.items():
            bucket[count-1].append(num)
        
        res = []
        for buc in bucket[::-1]:
            for i in buc:
                res.append(i)
                if len(res) == k: return res
