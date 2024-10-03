class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        pre = {}

        for i, value in enumerate(nums):
            remaining = target - nums[i]

            if remaining in pre:
                return [i, pre[remaining]]
            else:
                pre[value] = i


                
