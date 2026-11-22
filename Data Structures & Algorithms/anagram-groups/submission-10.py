class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        adict = defaultdict(list)

        for i in strs:
            temp = str(sorted(list(i)))
            adict[temp].append(i)
        return list(adict.values())
        