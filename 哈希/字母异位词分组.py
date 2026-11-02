class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mp = {}
        for s in strs:
            ss = "".join(sorted(s))
            if ss not in mp:
                mp[ss] = []
            mp[ss].append(s)
        res = list(mp.values())
        return res