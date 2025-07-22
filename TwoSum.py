class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_list = []
        for i in range(len(nums)):
            if target == nums[i] + nums[i+1]:
                return i, i+1
            else: i+1
