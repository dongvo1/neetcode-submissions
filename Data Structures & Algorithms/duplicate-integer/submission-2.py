class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # [1, 2, 3, 4]
        # set stores # at O(1) time
        # access at O(1) time

        vis = set()

        # vis = []

        for i in range(0, len(nums), 1):
            if (nums[i] in vis):
                return True
            vis.add(nums[i])
        return False

        