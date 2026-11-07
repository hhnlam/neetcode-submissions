class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        res = 0
        count = defaultdict(int)
        max_freq = 0

        for right in range(len(s)):
            count[s[right]] += 1
            window_length = right - left + 1
            max_freq = max(max_freq, count[s[right]])
            if window_length - max_freq > k:
                count[s[left]] -= 1
                left += 1
            else: res = max(res, window_length)
        
        return res