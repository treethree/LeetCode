# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)
        merged = []
        for i in intervals:
            if not merged or merged[-1].end < i.start:
                merged.append(i)
            else:
                merged[-1].end = max(merged[-1].end, i.end)
        return merged
# Time: O(nlgn) Space: O(1)
