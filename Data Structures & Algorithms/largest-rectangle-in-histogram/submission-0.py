class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """Find the largest area that can be formed in a histogram."""
        stack = []
        max_area = 0
        for idx, height in enumerate(heights):
            start = idx
            while stack and height < stack[-1][1]:
                top_index, top_height = stack.pop()
                max_area = max(top_height * (idx - top_index), max_area)
                start = top_index
            stack.append((start, height))

        for curr_i, curr_height in stack:
            max_area = max(max_area, curr_height * (len(heights) - curr_i))
        
        return max_area
