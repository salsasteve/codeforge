class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ans = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                # same value as before
                # and pointer1 is greater than 0
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                # p1 + l + r = 0
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0: # [-2,0,3,4,3]
                    # sum i too big  a l     r
                    # reduce it by decrementing the right pointer
                    r -= 1
                elif threeSum < 0 :# [-2,0,3,4,1]
                    # sum i too small  a l     r
                    # increment it by increase the left pointer
                    l += 1
                else:
                    ans.append([a, nums[l], nums[r]])
                    # [-2 , 2, 0, 0, 2, 2]
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return ans

        
        