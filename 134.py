class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if(sum(gas) < sum(cost)):
            return -1
        start = 0
        current_gas = 0
        for i in range(len(gas)):
            if current_gas < 0:
                start = i
                current_gas = 0
            current_gas += gas[i] - cost[i]

        return start