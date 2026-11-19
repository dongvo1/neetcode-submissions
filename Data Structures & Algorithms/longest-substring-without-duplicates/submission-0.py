class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # zxyzabxdf

        # yzabxdf

        # zxyabydf

        # zxyay
        vis = set()
        l = 0
        ans = 0
        for r in range(len(s)):
            while s[r] in vis:
                vis.remove(s[l])
                l += 1
            # print(s[l:r+1])
            ans = max(ans, r-l+1)
            vis.add(s[r])
        return ans