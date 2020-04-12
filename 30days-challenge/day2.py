# Happy Number
class Solution:
    def calcHappy(self, num) -> int:
        sam = rem = 0
        while(num > 0):
            rem = num % 10  # remainder
            sam = sam + (rem*rem)
            num = num//10  # divider
        return sam

    def isHappy(self, n: int) -> bool:
        nam = 0
        nam = self.calcHappy(n)
        while (nam != 1 and nam != 4):
            nam = self.calcHappy(nam)
        if nam == 1:
            return True
        elif nam == 4:
            return False
        # print(self.calcHappy(n))
