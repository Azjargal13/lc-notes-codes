# https://leetcode.com/problems/smallest-range-ii/
# 910. Smallest Range II


def smallestRangeII(A: [int], K: int) -> int:
    # need to get rid of multiple occurrences
    # from collections import Counter
    # cnt = Counter(A)
    # b = []
    # for i in cnt.keys():
    #     print(i)
    #     if i > K:
    #         b.append(i-K)
    #     else:
    #         b.append(i+K)
    # print(b)
    # return max(b) - min(b)

    A.sort()
    n = len(A)
    b = A[n-1]-A[0]
    for i in range(n-1):
        mx = max(A[i]+K, A[n-1]-K)
        mn = min(A[i+1]-K, A[0]+K)
        b = min(b, mx-mn)

    return b


A = [2, 7, 2]
K = 1
print(smallestRangeII(A, K))
