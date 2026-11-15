class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tdict = defaultdict(int)

        for i in range(len(nums)):
            if target - nums[i] in tdict:
                return [tdict[target - nums[i]], i]
            tdict[nums[i]] = i
        return []
        