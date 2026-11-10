class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dict
        # loop
        # see += 1
        # 1:1, 2:2, 3:3 

        # sort the values
        # return k most freq

        # [(1,1), (2, 2), (3,3)].sort(reverse=True) -> 
        # 


        kdict = defaultdict(int)

        for i in nums:
            kdict[i] += 1
        # print(kdict.items())
        return [k for k, v in reversed(sorted(kdict.items(), key=lambda x: x[1]))][:k]

        