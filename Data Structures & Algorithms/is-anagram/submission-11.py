class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = defaultdict(int) # auto create a value if the key does not exist
        tdict = defaultdict(int)

        for i in s:
            sdict[i] += 1 # sdict[pass in key] = value
        
        for i in t:
            tdict[i] += 1
            
        return sdict == tdict

        