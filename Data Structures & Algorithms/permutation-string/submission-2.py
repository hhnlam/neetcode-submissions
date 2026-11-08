class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        left = 0
        count_s = [0] * 26
        window_s = [0] * 26
        match = 0

        for s in range(len(s1)):
            count_s[ord(s1[s]) - ord('a')] += 1
            window_s[ord(s2[s]) - ord('a')] += 1
        
        for i in range(26):
            match += 1 if count_s[i] == window_s[i] else 0

        for right in range(len(s1), len(s2)):
            if match == 26: return True
            
            index = ord(s2[right]) - ord('a')
            window_s[index] += 1
            if window_s[index] == count_s[index]: match += 1
            elif window_s[index] == count_s[index] + 1: match -= 1
            
            index = ord(s2[left]) - ord('a')
            window_s[index] -= 1
            if window_s[index] == count_s[index]: match += 1
            elif window_s[index] == count_s[index] - 1: match -= 1
            left += 1
        return match == 26
            

