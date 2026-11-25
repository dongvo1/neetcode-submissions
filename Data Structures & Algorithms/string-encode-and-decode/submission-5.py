class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        return res


    def decode(self, s: str) -> List[str]:
        # "5#hello6#worlds"
        ans = []
        i = 0
        while i < len(s):     # loop through string

            leni = 0
            while s[i] != "#":   # trying to get the digit in front of #
                leni = leni*10 + int(s[i])    # finding the len of the word
                i += 1           
            i += 1               # skip over the #

            word = ""
            for j in range(leni):    # get the word
                word += s[i]
                i += 1
            ans.append(word)         # add words to array

        return ans

