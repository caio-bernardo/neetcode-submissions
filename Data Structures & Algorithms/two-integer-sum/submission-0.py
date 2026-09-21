class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        memo = {}
        for i in range(0, n):
            diff = target - nums[i]
            if diff in memo.keys():
                return [memo[diff], i]
            else:
                memo[nums[i]] = i
        return []