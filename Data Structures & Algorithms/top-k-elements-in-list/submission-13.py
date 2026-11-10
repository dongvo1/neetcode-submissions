class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        kdict = defaultdict(int)

        for i in nums:
            kdict[i] += 1   # add to dict

        arr = []
        for key, value in kdict.items():
            arr.append((value, key))  # add value, key to arr as a tuple
        arr.sort()
        arr.reverse()       

        karr = []
        for i in range(k):
            karr.append(arr[i][1])
        return karr


        


        
        