class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # mapy {}
        # check for thres hold passing
        # thres = []
        # increment mapy items or add item in a loop
        # return thres 

        mapy = {}
        thres = {}

        for i in range(len(nums)):
            q = nums[i]
            # add items to amp for memory of maxes
            if q in mapy:
                mapy[q] += 1
            else:
                mapy[q] = 1
            
        # {1:3,2:2,3:1}

        r = sorted(mapy.items(), key=lambda x:x[1], reverse=True)[:k] 
        print(r)

        return [x[0] for x in r]


            


            
            


     