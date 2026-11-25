class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kdict = defaultdict(int)

        for i in nums:
            kdict[i] += 1

        arr = []    
        for key, value in kdict.items():
            arr.append((value, key))
        arr.sort(reverse=True)

        ans = []
        for i in range(k):
            ans.append(arr[i][1])
        return ans