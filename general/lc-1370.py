# 1370. Increasing Decreasing String
# https://leetcode.com/problems/increasing-decreasing-string/


# pick smallest from s append it to the result
# pick smallest which is greater than last appended char -> repeat until can not pick more char
# pick largest append res
# pick largest which is smaller than last append char -> repeat until can not pick more char
# repeat till to pick all char

def sortString(s: str) -> str:
    from collections import Counter
    import string
    count, res = Counter(s), []
    print(count)

    while count:
        for el in string.ascii_lowercase, reversed(string.ascii_lowercase):
            for c in el:
                if c in count:
                    res += c
                    print(c, count, el)
            #res += [c for c in el if c in count]
            # print(res)
            count -= dict.fromkeys(count, 1)
    return "".join(res)


ss = "aaaabbbbcccc"
print(sortString(ss))
