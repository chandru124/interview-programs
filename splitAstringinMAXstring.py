class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balancedcount=0
        count=0
        for i in range(len(s)):
            current=s[i]
            if current=='L':    
                count+=1
            elif current=='R':
                count-=1
            
            if count==0:
                balancedcount+=1
                
        return balancedcount
