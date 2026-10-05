class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            res.append(f'{len(string)}#{string}')
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            idx = s.find('#', i)
            len_s = int(s[i:idx])
            word_start = idx + 1
            res.append(s[word_start:word_start+len_s])
            i = word_start + len_s
        return res

