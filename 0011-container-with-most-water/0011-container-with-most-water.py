class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        lp = 0
        rp = len(height) - 1
        maxi = 0

        while lp < rp:
            width  = rp - lp 
            h = min(height[lp], height[rp])
            
            calc = width*h

            maxi = max(maxi, calc)

            if height[lp] > height[rp]:
                rp -= 1
            else:
                lp += 1
                
        return maxi



