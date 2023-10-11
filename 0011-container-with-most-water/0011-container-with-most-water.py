class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        l = 0 # height of the left stick
        r = len(height) - 1 # height of the right stick

        # max(height) * length(r-l)
        max_area = 0

        while l < r:
            length = r - l
            cur_min_height = min(height[l], height[r])

            area = length * cur_min_height

            max_area = max(max_area, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
            

        

        
            




