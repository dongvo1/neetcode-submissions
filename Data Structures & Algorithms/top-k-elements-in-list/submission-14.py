class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # keep a freqeuncy of elements
        # sort all as (frequency, key)
        # return only the keys
        
        # number -> frequency
        freq = defaultdict(int)
        for i in range(len(nums)):
            freq[nums[i]] += 1

        # (frequency, number)
        arr = []
        for key,val in freq.items():
            arr.append((val,key))
        arr.sort(reverse=True)

        # number
        ans = []
        for i in range(k):
            ans.append(arr[i][1])
        return ans