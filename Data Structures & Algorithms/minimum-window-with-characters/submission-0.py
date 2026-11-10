class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        count_t = defaultdict(int)
        window_s = defaultdict(int)
        
        for i in range(len(t)):
            count_t[t[i]] += 1
        
        left = 0
        match = 0
        need = len(count_t)
        res = [-1, -1]
        res_len = float('inf')
        for right in range(len(s)):
            window_s[s[right]] += 1

            if window_s[s[right]] == count_t[s[right]]:
                match += 1
            
            while match == need:
                if right - left + 1 < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                window_s[s[left]] -= 1
                if window_s[s[left]] < count_t[s[left]]: 
                    match -= 1
                left += 1
        l, r = res
        return s[l:r+1] if res_len != float('inf') else ""

