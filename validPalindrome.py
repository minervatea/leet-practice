class Solution:
    def validPalindrome(self, s: str) -> bool:
      for i in range(len(s)):
        removed = s[:i] + s[i+1:]
        if(self._isPalindrome(removed)):
          return True
      return False
    
    
    def _isPalindrome(self, s: str) -> bool:
        return s == s[::-1]
s = Solution()
print(s.validPalindrome("tebbem"))