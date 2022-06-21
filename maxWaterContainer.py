class Solution:
    def maxArea(self, height: List[int]) -> int:
        pointer_l = 0
        pointer_r = len(height) - 1
        
        max_water = 0
        
        while(pointer_l < pointer_r):
            if(height[pointer_l] <= height[pointer_r]):
                cur_max = height[pointer_l] * (pointer_r - pointer_l)
                pointer_l += 1
            else:
                cur_max = height[pointer_r] * (pointer_r - pointer_l)
                pointer_r -= 1
            
            if(cur_max > max_water):
                max_water = cur_max
                
        return max_water