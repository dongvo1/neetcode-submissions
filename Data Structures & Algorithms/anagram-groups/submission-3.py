class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use dict
        # loop through list 
        # sort the word by converting from string to list and back to string
        # add sorted string as key and append all strings that share same key
        # return dict value as list
        
        adict = defaultdict(list) 

        for i in range(len(strs)):                    # loop through list
            strs_sorted = ''.join(sorted(strs[i]))    # turn string into list and sort 
                                                      # in order and join back to 
                                                      # string
            adict[strs_sorted].append(strs[i])        # is key in dict, yes append, no 
                                                      # create new key, append
        return list(adict.values())                   




