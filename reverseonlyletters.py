class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s1 = ""
        for x in s:
            if x.isalpha():
                s1 += x
        s2 = s1[::-1]
        s3 = ""
        k = 0
        for i in range(len(s)):
            if s[i].isalpha():
                s3 += s2[k]
                k += 1
            else:
                s3 += s[i]
        return s3
        
