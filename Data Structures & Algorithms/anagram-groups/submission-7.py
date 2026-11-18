class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary:
        # normalize words -> list of words

        sdict = defaultdict(list)

        for i in strs:
            normalized = str(sorted(list(i)))
            sdict[normalized].append(i)
        
        return list(sdict.values())
