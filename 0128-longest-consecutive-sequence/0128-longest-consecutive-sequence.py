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

        for n in nums:
            if (n - 1) not in nums_set:
                # maybe the start of a sequence
                length = 1
                while (n + length) in nums_set:
                    length += 1
                longest = max(length, longest)

        return longest 






