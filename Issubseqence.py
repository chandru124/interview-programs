class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lt = 0         
        cnt = 0        
        for c in s:
            for i in range(lt, len(t)):
                if t[i] == c:
                    lt = i + 1
                    cnt += 1
                    break
            if lt >= len(t):
                break
        return cnt == len(s)
