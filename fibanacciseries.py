class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=0
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        return self.fib(n-1)+self.fib(n-2)
        
  
