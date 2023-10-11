class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        water = 0
        
        l = 0
        r = len(height) - 1

        max_left = height[0]
        max_right = height[len(height) - 1]

        

        while l < r :
            
            if height[l] < height[r]:
                l += 1
                max_left = max(height[l], max_left)
                water += max_left - height[l]
            else:
                r -= 1
                max_right = max(height[r], max_right)
                water += max_right - height[r]


        return water



    


        



        