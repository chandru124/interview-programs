class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums=0
        for i in nums:
            sums += i
        
        n=len(nums)+1
        return (n *(n-1) /2) - sums
