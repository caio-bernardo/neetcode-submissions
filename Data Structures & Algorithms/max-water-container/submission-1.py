class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0

        left = 0
        right = n - 1
        while left < right:
            h = min(heights[left], heights[right])
            w = right - left
            a = w * h
            max_area = max(a, max_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area