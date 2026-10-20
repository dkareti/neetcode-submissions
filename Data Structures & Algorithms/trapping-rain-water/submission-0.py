class Solution:
    def trap(self, height: List[int]) -> int:
        """Find the total amount of water that can be collected."""
        #### BASE CASE ####
        if len(height) == 1:
            return 0

        #### POINTERS ####
        left = 0
        total_area = 0

        maximum_left = [0] * len(height)
        #### Find the maximum of a left subarray
        for i in range(len(height)):
            if i > 0:
                maximum_left[i] = max(maximum_left[i - 1], height[i-1])
        
        maximum_right = [0] * len(height)
        #### Find the maximum of a left subarray
        for i in range(len(height) - 1, -1, -1):
            if i < len(height) - 1:
                maximum_right[i] = max(maximum_right[ i + 1 ], height[i + 1])

        for right, height_i in enumerate(height):
            # Find the max of the left subarray and the max of the right subarray
            value = min(maximum_left[right], maximum_right[right]) - height_i
            total_area = total_area + value if value >= 0 else total_area + 0  

        return total_area
            
