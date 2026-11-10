class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kdict = defaultdict(int)

        for i in nums:
            kdict[i] += 1
        # print(kdict.items())

        arr = []
        for key, value in kdict.items():
            arr.append((value, key))
        arr.sort()
        arr.reverse()

        karr = []
        for i in range(0, k, 1):
            karr.append(arr[i][1])
        return karr


        