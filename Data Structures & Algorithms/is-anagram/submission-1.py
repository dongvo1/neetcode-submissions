class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # dict (key -> pair value)
        # loop through string 
        # for every letter create a new key -> value pair
        # defaultdict assign deafult value to any key that does not exist yet
        # if key exist add one to value

        sdict = defaultdict()
        tdict = defaultdict()

        for i in s:
            sdict[i] = sdict.get(i,0) + 1

        for i in t:
            tdict[i] = tdict.get(i,0) + 1

        if sdict.items() == tdict.items():
            return True
        return False


        