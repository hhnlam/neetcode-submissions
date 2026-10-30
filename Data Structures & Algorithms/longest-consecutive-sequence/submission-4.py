class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_counter = 0
        max_num = len(nums)

        for num in nums_set:
            if num-1 not in nums_set: 
                counter = 1
                current_num = num
                while current_num + 1 in nums_set:
                    counter += 1
                    current_num += 1
                if counter > max_counter: max_counter = counter

        return max_counter
