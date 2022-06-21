import copy

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:

      cnt = 0
      flowerbed = [0] + flowerbed + [0]

      for i in range(len(flowerbed)-1):
        if(flowerbed[i] == 0 and flowerbed[i-1] == 1 and flowerbed[i+1] == 1):
            continue
        else:
            flowerbed[i] = 1
            cnt += 1 
        
      return cnt >= n



s = Solution()
print(s.canPlaceFlowers([0,0,1,0,1],1))


