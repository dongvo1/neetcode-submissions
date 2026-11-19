class Solution:

    def encode(self, strs: List[str]) -> str:

        ans = ""
        for i in strs:
            ans += str(len(i)) + "#"
            ans += i
        return ans

    def decode(self, s: str) -> List[str]:

        ans = []
        i = 0
        while i < len(s):

            leni = 0
            while s[i] != '#':
                leni = leni*10 + int(s[i])
                i += 1
            i += 1 

            word = ""
            for j in range(leni):
                word += s[i]
                i += 1
            ans.append(word)
        return ans
                



# [6Hello, 5World]

# 6#6Hello6#5World