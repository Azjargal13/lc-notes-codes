# 452. Minimum Number of Arrows to Burst Balloons


# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

def findMinArrowShots(points: [[int]]) -> int:
    # sort by left coord then by width
    p = sorted(sorted(points), key=lambda x: (x[1], x[1]-x[0]))
    # print(p)
    c = 0
    last_shot = 0

    for i in p:
        if(i[0] >= last_shot):
            last_shot = i[1]
            c += 1
    return c


p = [[7, 10], [1, 5], [3, 6], [2, 4], [1, 4]]
print(findMinArrowShots(p))
