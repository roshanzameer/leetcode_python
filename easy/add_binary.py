# https://leetcode.com/problems/add-binary/

# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"


def addBinary(a: str, b: str):

    if a == b == '0':
        return a

    a_dec = 0
    a = a[::-1]
    for i in range(len(a)):
        prod = int(a[i]) * (2 ** i)
        a_dec += prod


    b_dec = 0
    b = b[::-1]
    for i in range(len(b)):
        b_dec += (int(b[i]) * (2 ** i))

    res_dec = a_dec + b_dec

    res_binary = []

    i = 0
    while res_dec > 0:
        res_binary.insert(0, res_dec % 2)
        res_dec = res_dec // 2

        i += 1
    
    return ''.join([str(i) for i in res_binary])


print(addBinary("0","0"))



bin_chart = [64, 32, 16, 8, 4, 2, 1]
bin_chart = bin_chart[::-1]


a = '1101' # 13
a= a[::-1]
a_dec = 0
for i in zip(a, bin_chart):
    print(i)
    if i[0] == '1':
        a_dec += i[1]
        print('//', a_dec)

print(a_dec)
