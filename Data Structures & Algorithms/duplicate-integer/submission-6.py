class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # create a set
        # loop through list check in set
        # if not in set add to set
        # if in set return true
        # time complexity O(n)
        # space complexity O(n)

        vis = set()

        for i in range(len(nums)):
            if(nums[i] in vis):
                return True
            vis.add(nums[i])
        return False