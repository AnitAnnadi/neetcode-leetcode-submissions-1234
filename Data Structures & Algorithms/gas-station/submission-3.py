class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start, currSum = 0, 0
        for i in range(len(gas)):
            if currSum < 0:
                currSum, start = 0, i
            currSum += gas[i] - cost[i]

        return start