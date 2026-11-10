class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dict
        # loop through list
        # sort each value
        # add to dict
        # return list of values

        adict = defaultdict(list)

        for i in range(len(strs)):
            strs_sorted = "".join(sorted(strs[i]))
            adict[strs_sorted].append(strs[i])
        return list(adict.values())
        

        