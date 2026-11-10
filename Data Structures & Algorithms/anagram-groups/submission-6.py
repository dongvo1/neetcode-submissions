class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        adict = defaultdict(list)

        for i in strs:
            strs_sorted = str(sorted(i))
            adict[strs_sorted].append(i)
        return list(adict.values())