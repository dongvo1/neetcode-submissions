class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # letters as keys
        # counts as values
        sdict = {}
        tdict = {}

        for i in range(len(s)):
            if s[i] in sdict:
                sdict[s[i]] += 1
                continue
            sdict[s[i]] = 1

        for i in range(len(t)):
            if t[i] in tdict:
                tdict[t[i]] += 1
                continue
            tdict[t[i]] = 1

        if sdict == tdict:
            return True
        return False

        