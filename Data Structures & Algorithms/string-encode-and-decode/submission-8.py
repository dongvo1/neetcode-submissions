class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        return res

    def decode(self, s: str) -> List[str]:
        "5#hello6#worlds"
        ans  = []
        i = 0

        while i < len(s):
            length = 0
            while s[i] != "#":
                length = length * 10 + int(s[i]) # 12
                i += 1
            i += 1

            word = ""
            for j in range(length):
                word += s[i]
                i += 1
            ans.append(word)

        return ans

