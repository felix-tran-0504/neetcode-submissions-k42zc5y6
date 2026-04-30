class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def d(s: str):
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            return tuple(count)
        res = defaultdict(list)
        for s in strs:
            s_dict = d(s)
            res[s_dict].append(s)
        return list(res.values())