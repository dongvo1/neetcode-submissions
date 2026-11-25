class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [1,1,2,2,3,3,4]
        fdict = defaultdict(int)

        for i in nums:                # {1:2, 2:2, 3:2, 4:1}
            fdict[i] += 1           

        arr = []
        for key, value in fdict.items():
            arr.append((value, key))  # [(2,1), (2,2), (2,3), (4,1)]
        arr.sort(reverse=True)

        ans = []
        for i in range(k):
            ans.append(arr[i][1])
        
        return ans