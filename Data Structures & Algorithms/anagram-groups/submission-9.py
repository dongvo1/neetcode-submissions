class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dict
        # key -> act
        # value -> act , cat

        adict = defaultdict(list)

        for i in strs:
            temp = str(sorted(list(i)))
            adict[temp].append(i)
        
        return list(adict.values())