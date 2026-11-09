class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        smap = defaultdict(int)
        tmap = defaultdict(int) #{}

        for i in s:
            smap[i] += 1

        for i in range (0, len(t), 1):
            letter = t[i]
            if (letter not in tmap):
                tmap[letter] = 1
            else:
                tmap[letter] += 1

        if tmap == smap:
            return True
        return False
        

        