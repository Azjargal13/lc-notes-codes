# third task
# happy longest number


def longestDiverseString(a: int, b: int, c: int) -> str:
    res = []

    # by freq
    all_val = [['a', a], ['b', b], ['c', c]]
    #
    #all_char = 'a' * a + 'b' * b + 'c'*c

    # sort all_val by its value
    all_val.sort(key=lambda el: -el[1])
    # [['c', 7], ['b', 1], ['a', 1]]

    while(all_val[0][1]):
        if len(res) >= 2 and res[-1] == res[-2] and res[-1] == all_val[0][0]:
            if all_val[1][1] == 0:
                break
            # go to next array
            all_val[1][1] -= 1
            res.append(all_val[1][0])
        else:
            print(all_val[0][1])
            all_val[0][1] -= 1
            print(all_val[0][1])
            res.append(all_val[0][0])
        all_val.sort(key=lambda x: -x[1])
        # [['c', 7], ['b', 1], ['a', 0]]
        print(all_val)
        print(res)
    print(all_val[0][1])
    return "".join(res)


print(longestDiverseString(a=1, b=1, c=7))
