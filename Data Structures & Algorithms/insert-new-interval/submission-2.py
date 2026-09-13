class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #Brute
        '''intervals.append(newInterval)
        intervals.sort()
        i = 0
        while i < len(intervals)-1:
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max(intervals[i][1],intervals[i+1][1])
                intervals.remove(intervals[i+1])
            else:
                i += 1
        return intervals'''

        #optimal - avoid sorting
        result = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0],intervals[i][0])
            newInterval[1] = max(newInterval[1],intervals[i][1])
            i += 1

        result.append(newInterval)
        result.extend(intervals[i:])

        return result












        