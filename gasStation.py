import collections

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        s_points = [idx for idx, value in enumerate(gas) if value >= cost[idx]]

        ans = -1
        gas_queue = collections.deque(gas)
        cost_queue = collections.deque(cost)

        for s in s_points:
            
            if(ans != -1):
                break
            
            remain_gas = 0
            
            for step in range(len(gas)):
                if(remain_gas + list(gas_queue)[s] >= list(cost_queue)[s]):
                    remain_gas = remain_gas + (list(gas_queue)[s] -  list(cost_queue)[s])
                    # next one in queue
                    gas_queue.rotate(-1)
                    cost_queue.rotate(-1)
                else:
                    break
            
            ans = s
        return ans

        


      
s = Solution()
print(s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))

