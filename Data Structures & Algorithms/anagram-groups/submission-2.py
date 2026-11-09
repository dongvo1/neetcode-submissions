class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use dict
        # loop throught list 
        # sort the word by converting from string to list and back to string
        # add sorted string as key and append all strings that share same key
        # return value pair in list
        
        adict = defaultdict(list)

        for i in range(len(strs)):
            strs_sorted = ''.join(sorted(strs[i]))
            adict[strs_sorted].append(strs[i])
        return list(adict.values())
            




