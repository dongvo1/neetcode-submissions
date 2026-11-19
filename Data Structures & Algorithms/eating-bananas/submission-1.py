class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # 5 10 12 15 16 25 30 100 1000
        # 0 0  0  0  0  1  1  1    1

        def check(num):
            ans = 0
            for i in piles:
                ans += (i+num-1)//num
            return ans <= h

        l, r = 1, max(piles)

        while l < r:
            mid = (l+r)//2

            if check(mid):
                r = mid
            else:
                l = mid+1
                
        return l


        # [25,10,23,4]

        # [3, 1, 3, 1] = 8