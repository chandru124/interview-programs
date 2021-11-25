import sys
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        c=[sys.maxint] * len(nums)
        c[0]=0
        for i in range(len(nums)-1):
            k=nums[i]
            j=1
            while j<=k and i+j<len(nums):
                c[i+j]=min(c[i+j],c[i]+1)
                j+=1
        return c[len(nums)-1]
                
