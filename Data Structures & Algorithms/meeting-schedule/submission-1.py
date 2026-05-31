"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True

        maxStart = -1
        minEnd = -1

        for interval in sorted(intervals, key=lambda c: c.start):
            if interval.start < maxStart and interval.end <= maxStart:
                maxStart = interval.start
            elif interval.end > minEnd and interval.start >= minEnd:
                minEnd = interval.end
            else:
                return False

        return True
