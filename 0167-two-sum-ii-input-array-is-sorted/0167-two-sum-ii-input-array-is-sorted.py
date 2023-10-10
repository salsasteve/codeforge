class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # loop and hold on to the number till you 
        # know for sure you can release it or findme = target - first > cur
        
        left, right = 0, len(numbers) - 1

        while left < right:

            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
            # Return indices as 1-indexed
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    # The problem guarantees one solution, so we won't reach this point.
        return []
            






            
        