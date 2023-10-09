class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # start of sequences dont have a left neighbor
        # create a set for O(n) look up times

        nums_set = set(nums)
        longest = 0

        for i in nums:
            if i-1 not in nums_set:
                # maybe the start of a sequence
                tmp = 1
                while i+tmp in nums_set:
                    tmp += 1
                if tmp > longest:
                    longest = tmp

        return longest 






