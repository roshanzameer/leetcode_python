
def is_substring():
    str1 = "onetwofour"
    str2 = "hellofourtwooneworld"

    res = 0
    i = 0
    j = len(str1)
    while i < len(str2) - len(str1) +1: 
        print(str2[i:j])
        substring = str2[i:j]
        if sorted(str1) == sorted(substring):
            res += 1
        i+=1
        j+=1

    return res

print(is_substring())






