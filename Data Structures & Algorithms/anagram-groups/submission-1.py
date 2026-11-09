class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use dict
        # loop throught list 
        # take in an index, map letters to how many times they repeat
        # sort the word by abc compare key
        # if match add to sublist
        # return sublist
        
        adict = defaultdict(list)

        for i in range(len(strs)):
            strs_sorted = ''.join(sorted(strs[i]))
            adict[strs_sorted].append(strs[i])
        return list(adict.values())
            




