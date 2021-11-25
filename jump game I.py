class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        minStepsRequired = 0
        previousGood = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            minStepsRequired = previousGood - i
            if nums[i] >= minStepsRequired:
                    previousGood = i
    return previousGood == 0
                
