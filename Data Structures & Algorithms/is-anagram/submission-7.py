class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # letters as keys
        # counts as values

        sdict = defaultdict(int)
        tdict = defaultdict(int)

        for i in s:
            sdict[i] += 1

        for i in t:
            tdict[i] += 1

        return sdict == tdict
        