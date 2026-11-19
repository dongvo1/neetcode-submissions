class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # keep track of frequent
        fdict = defaultdict(int)

        for i in nums:
            fdict[i] += 1

        # flip + sort key value
        arr = []
        for key, value in fdict.items():
            arr.append((value, key))
        arr.sort(reverse=True)

        # return value
        ans = []
        for i in range(k):
            ans.append(arr[i][1])
        return ans

        