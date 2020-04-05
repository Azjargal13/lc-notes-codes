# second task
# https://leetcode.com/contest/weekly-contest-183/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/.


def numSteps(s: str) -> int:
    integ = 0
    #dec = int(s, 2)
    leng = len(s)
    for i in range(leng):
        integ += int(s[leng-1-i])*pow(2, i)
    print(integ)

    counter = 0
    while (integ != 1):
        if integ % 2 == 0:
            integ //= 2
        else:
            integ += 1
        counter += 1
    print(counter)


numSteps(s="1111011110000011100000110001011011110010111001010111110001")
