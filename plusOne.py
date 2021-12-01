class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for index,value in enumerate(digits[::-1]):
            if value < 9:
                digits[~index] += 1
                return digits
            else:
                digits[~index] = 0
        
        return [1] + digits
