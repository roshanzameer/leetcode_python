def isAnagram(s, t):

    if len(s) != len(t):
        return False
    
    count_s, count_t = {}, {}
    
    for i in range(len(s)):
        
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)
        
        print(count_s)
        print(count_t)

    for el in count_s:
        print(count_s.get(el), count_t.get(el))
        if count_s[el] != count_t.get(el, 0):
            return False
        
    return True


print(isAnagram('anagram', 'nagaram'))