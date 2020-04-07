# 435. Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals/


def eraseOverlapIntervals(intervals: [[int]]) -> int:
    interval = sorted(intervals, key=lambda x: (x[1]))
    if len(intervals) < 2:
        return 0
    c = 0
    ref = 0
    for i in interval:
        if i[0] >= ref:
            ref = i[1]
        else:
            c += 1
    return c


interval = [[1, 100], [11, 22], [1, 11], [2, 12]]
print(eraseOverlapIntervals(interval))
