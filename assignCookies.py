class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        
        g,s = sorted(g), sorted(s)

        cookiei, childi = 0,0

        while cookiei < len(s) and childi < len(g):        
            if s[cookiei] >= g[childi]:
                childi += 1
            cookiei += 1
        
        return childi