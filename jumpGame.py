class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1
        pointer = len(nums) - 2

        while pointer > 0 :
            if nums[pointer] >= goal - pointer:
                goal = pointer
                pointer-=1
            pointer-=1
                
        return pointer == -1


s = Solution()
print(s.canJump([2,3,1,1,4]))

print(s.canJump([3,2,1,0,4]))
        
