class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # vis = set()

        # for i in range (0,len(nums), 1):
        #     if (nums[i] in vis):
        #         return True
        #     vis.add(nums[i])
        # return False

        vis = set(nums)
        if (len(vis) != len(nums)):
            return True
        return False