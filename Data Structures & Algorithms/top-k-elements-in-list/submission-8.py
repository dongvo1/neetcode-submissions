class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kdict = Counter(nums)
        # print(kdict.items())
        maxi = max(kdict.values())+1
        buckets = [[] for _ in range(maxi)]

        for key, value in kdict.items():
            buckets[value].append(key)
        cnt = 0
        ans = []
        for i in range(maxi-1, -1, -1):
            for j in buckets[i]:
                ans.append(j)
                if len(ans) >= k:
                    return ans
        return ans[:k]


