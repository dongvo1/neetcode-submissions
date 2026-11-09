class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmap = defaultdict(int)

        for i in range(len(nums)):
            if (target - nums[i]) in tmap:
                return [tmap[target - nums[i]], i]
            tmap[nums[i]] = i
        return []