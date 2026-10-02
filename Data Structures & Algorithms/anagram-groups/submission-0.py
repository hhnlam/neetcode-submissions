class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for string in strs:
            temp_map = [0] * 26
            for s in string:
                temp_map[ord(s) - ord('a')] += 1
            anagram_map[tuple(temp_map)].append(string)
        return list(anagram_map.values())
