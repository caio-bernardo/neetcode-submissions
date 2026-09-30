class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniques = set(nums)
        longest = 0

        for i in uniques:
            if (i - 1) not in uniques:
                length = 1
                while i + length in uniques:
                    length += 1
                longest = max(longest, length)
        return longest