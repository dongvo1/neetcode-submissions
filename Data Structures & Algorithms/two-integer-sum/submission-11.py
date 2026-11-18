class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # loop through nums
        # value of nums -> key dict
        # index -> value dict
        # if target - nums[i] alr in dict
        # return indices
        # first value -> tdict[target - nums[i]]
        # second value -> i
 
        tdict = defaultdict(int)

        for i in range(len(nums)):
            if target - nums[i] in tdict:
                return [tdict[target - nums[i]], i]
            tdict[nums[i]] = i
        return []

