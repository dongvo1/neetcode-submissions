class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        imap = defaultdict(int)

        # nums = [1, 2, 3, 4]
        # target = 5
        # imap = {}

        for i in range(0, len(nums), 1):
            if(target - nums[i]) in imap:
                return [imap[target - nums[i]], i]    #array of the indexes
            imap[nums[i]] = i
        return []
        
