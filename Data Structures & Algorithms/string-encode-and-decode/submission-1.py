class Solution:

    def encode(self, strs: List[str]) -> str:
        # 96#
        cur = ""
        for i in strs:
            cur += str(len(i)) + "#"
            cur += i
        return cur

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            numi = 0
            while s[i] != "#":
                numi = numi*10+int(s[i])
                i += 1
            i += 1
            to = i + numi
            curstr = ""
            while i < to:
                curstr += s[i]
                i += 1
            ans.append(curstr)
        return ans