class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kdict = defaultdict(int)

        for i in nums:
            kdict[i] += 1
        # print(kdict.items())

        maxi = max(kdict.values())+1
        buckets = [[] for _ in range(maxi)]

        for key, value in kdict.items():
            buckets[value].append(key)
        cnt = 0
        ans = []
        for i in range(maxi-1, -1, -1):
            ans += buckets[i]
        return ans[:k]


