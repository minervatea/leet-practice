class Solution:
    def candy(self, ratings: list[int]) -> int:
    
        
        r_dir = {k: 1 for k, v in enumerate(ratings)}
        # l_dir = {k: 1 for k, v in enumerate(ratings)}
        # minimum = 0
        
        for i in range(0, len(ratings) - 1):
         if(ratings[i+1] - ratings[i] >= 1):
             r_dir[i+1] = r_dir[i] + 1   
        
        for i in range(len(ratings) - 1 , 0, -1):
            if(ratings[i-1] - ratings[i] >= 1):
                r_dir[i-1] = max(r_dir[i] + 1, r_dir[i-1])
        return sum(r_dir.values())
            

s = Solution()
print(s.candy([1,0,2]))
print(s.candy([1,2,87,87,87,2,1]))

