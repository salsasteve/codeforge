class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # Initial total trapped water
        trapped_water = 0
        
        # Pointers initialized at the leftmost and rightmost bars
        left_pointer, right_pointer = 0, len(height) - 1

        # Variables to keep track of the tallest bar from the left and right up to the current position
        max_left, max_right = height[left_pointer], height[right_pointer]

        # Iterate till the two pointers meet
        while left_pointer < right_pointer:
            
            # If the bar at the current left pointer is shorter than the bar at the current right pointer
            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
                max_left = max(height[left_pointer], max_left)  # Update max from the left
                trapped_water += max_left - height[left_pointer]  # Calculate trapped water at the current position
            else:
                # Do the same logic for the right pointer if the bar at the right pointer is shorter
                right_pointer -= 1
                max_right = max(height[right_pointer], max_right)
                trapped_water += max_right - height[right_pointer]

        return trapped_water
