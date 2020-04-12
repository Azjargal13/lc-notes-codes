# 5381. Queries on a Permutation With Key


class Solution:
    def processQueries(self, queries: [int], m: int) -> [int]:
        p = []
        for i in range(1, m+1):
            p.append(i)
        ret = []
        for i in queries:
            for k in range(len(p)):
                if p[k] == i:
                    ret.append(k)
                    # print(k)
                    a = p[k]
                    p.remove(p[k])
                    p.insert(0, a)
            # find i from p

        return ret
        # P = range(1, m + 1)
        # ans = []
        # for q in queries:
        #     i = P.index(q)
        #     ans.append(i)
        #     P2 = [P.pop(i)]
        #     P2.extend(P)
        #     P = P2
        # return ans


s = Solution()
queries = [7, 5, 5, 8, 3]
m = 8
print(s.processQueries(queries, m))
