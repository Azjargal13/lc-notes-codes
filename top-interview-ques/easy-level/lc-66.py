# Plus One
class Solution:
    def plusOne(self, digits):
        for i in range(len(digits)):
            if digits[~i] < 9:
                digits[~i] += 1
                return digits
            digits[~i] = 0
            # print([1]+[0]*len(digits))
        return [1] + [0] * len(digits)

        # result = []
        #     str_digits = ''.join(str(i) for i in digits)
        #     int_digits = int(str_digits) + 1
        #     str_digits = str(int_digits)
        #     for i in str_digits:
        #         result.append(int(i))
        #     return result

        # int_str = "".join(str(c) for c in digits)
        # res = int(int_str) + 1
        # res_l = [c for c in str(res)]
        # return res_l
s = Solution()
print(s.plusOne([1, 7, 9]))
