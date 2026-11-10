class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dict
        # loop through list
        # sort each value
        # add to dict
        # return list of values

        adict = defaultdict(list)

        for i in range(len(strs)):
            adict[str(sorted(strs[i]))].append(strs[i])
        return list(adict.values())
        

        