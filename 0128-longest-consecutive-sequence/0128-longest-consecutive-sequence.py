class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nn = set(nums)   
        out = None
        
        maxi = 0
        for i in nn:
            if i-1 not in nn:
                cl = 1
                while i+cl in nn:
                    cl += 1

                if cl > maxi:
                    maxi = cl
        return maxi
            





