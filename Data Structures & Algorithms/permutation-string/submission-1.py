class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        left = 0
        count_s = [0] * 26
        window_s = [0] * 26

        for s in s1:
            count_s[ord(s) - ord('a')] += 1

        for right in range(len(s2)):
            if right - left + 1 > len(s1):
                window_s[ord(s2[left]) - ord('a')] -= 1
                left += 1
            
            window_s[ord(s2[right]) - ord('a')] += 1
            
            if right - left + 1 == len(s1) and window_s == count_s: return True
        return False
            

