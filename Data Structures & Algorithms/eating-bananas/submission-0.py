class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        range_rate = [1, max(piles)]
        min_rate = float('inf')
        
        while range_rate[1] >= range_rate[0]:
            current_rate = (range_rate[1] + range_rate[0]) // 2
            hours = 0
            for i in piles:
                hours += math.ceil(i / current_rate)
            if hours <= h:
                if current_rate < min_rate: min_rate = current_rate
                range_rate[1] = current_rate - 1
            else:
                range_rate[0] = current_rate + 1
        return min_rate