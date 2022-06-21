
class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        palindromes = []

        curr = ""

        for char in s:
          curr += char

          if(self._isPalindrome(curr)):
            continue
          else:
            # add current palidrome and reset 
            palindromes.append(curr)
            curr = ""
  
            return max(palindromes, key=len)

    def _isPalindrome(self, s: str) -> bool:
      if len(s) % 2 == 0:
        start = len(s)//2

        for i in range(start):
          if(s[start+i] != s[start-1-i]):
            return False
        return True

      else:
        start = len(s)//2
        for i in range(start):
          if(s[start+i] != s[start-i]):
            return False
        return True

      

s = Solution()
print(s.longestPalindrome('abcccdd'))