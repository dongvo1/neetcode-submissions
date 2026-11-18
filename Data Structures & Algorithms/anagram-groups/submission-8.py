class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sdict = defaultdict(list)

        for i in strs:
            temp = str(sorted(list(i)))
            sdict[temp].append(i)
        
        return list(sdict.values())