class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1

        while l <= r:
            sumi = nums[l] + nums[r]
            # print(l,r)
            if sumi == target:
                return [l+1, r+1]
            elif sumi > target:
                r -= 1
            else:
                l += 1
        return []