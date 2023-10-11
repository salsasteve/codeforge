class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # Final list to store the resulting triplets
        triplets = []
        
        # Sort the input list
        nums.sort()
        
        # Iterate through the list
        for idx, num in enumerate(nums):
            # Skip duplicates
            if idx > 0 and num == nums[idx - 1]:
                continue
            
            # Two pointers initialized
            left, right = idx + 1, len(nums) - 1
            
            # Continue as long as left pointer is to the left of right pointer
            while left < right:
                current_sum = num + nums[left] + nums[right]
                
                # If the sum of the three numbers is greater than 0,
                # we need to decrease the sum, so we move the right pointer to the left
                if current_sum > 0:
                    right -= 1
                # If the sum of the three numbers is less than 0,
                # we need to increase the sum, so we move the left pointer to the right
                elif current_sum < 0:
                    left += 1
                # If the sum is zero, it's a valid triplet
                else:
                    triplets.append([num, nums[left], nums[right]])
                    left += 1
                    
                    # Skip duplicates on the left pointer side
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

        return triplets
