class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        intervals.sort()
        i,j = 0,1
        while j < len(intervals):
            if intervals[i][1] >= intervals[j][0]:
                while j < len(intervals) and intervals[i][1] >= intervals[j][0]:
                    end = intervals.pop(j)
                    intervals[i][1] = max(intervals[i][1],end[1])
            else:
                i += 1
                j += 1
        return intervals
        