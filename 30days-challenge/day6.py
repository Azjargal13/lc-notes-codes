# group anagrams


def groupAnagrams(strs: [str]) -> [[str]]:
    # runtime 204ms
    # dic = dict()
    # for i in strs:
    #     s = "".join(sorted(i))
    #     if s not in dic:
    #         dic[s] = [i]
    #     else:
    #         dic[s].append(i)
    # res = [val for val in dic.values()]
    # return res

    # runtime 100ms
    import collections
    ans_dict = collections.defaultdict(list)
    for i in strs:
        tmp = ''.join(sorted(i))
        ans_dict[tmp].append(i)
    return ans_dict.values()


s = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(s))
