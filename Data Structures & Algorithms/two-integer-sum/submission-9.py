class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmap = defaultdict(int)

        for i in range(len(nums)):                   # good
            if (target - nums[i]) in tmap:           # good
                return [tmap[target - nums[i]], i]   # 
            tmap[nums[i]] = i                        # storing value in the array 
            #tamp[key] = value                       # as a key in order to look up 
                                                     # the index
        return []