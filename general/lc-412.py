# 412. Fizz Buzz


class Solution:
    def fizzBuzz(self, n: int) -> [str]:
        res = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        # print(res)
        return res

        # using list comprehension
        # list_of_output = [ 'Fizz' * (not i % 3) + 'Buzz' * (not i % 5 ) or str(i) for i in range(1, n+1) ]

        # return list_of_output
s = Solution()

print(s.fizzBuzz(15))
