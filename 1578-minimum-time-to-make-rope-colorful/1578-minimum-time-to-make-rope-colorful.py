class Solution(object):
    def minCost(self, colors, neededTime):
        total_cost = 0
        group_sum = neededTime[0]
        group_max = neededTime[0]
        
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                group_sum += neededTime[i]
                group_max = max(group_max, neededTime[i])
            else:
                total_cost += group_sum - group_max
                group_sum = neededTime[i]
                group_max = neededTime[i]

        total_cost += group_sum - group_max
        return total_cost