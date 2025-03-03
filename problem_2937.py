#You are given three strings: s1, s2, and s3.
#In one operation you can choose one of these strings and delete its rightmost character.

def findMinimumOperations(s1,s2,s3):


    a = len(s1)
    b = len(s2)
    c = len(s3)
    m = min(a, b, c)
    d = 0
    for i in range(m):
        if s1[i] == s2[i] and s1[i] == s3[i]:
            d += 1
        else:
            break
    if d == 0:
        return -1
    return a + b + c - (3 * d)


output = findMinimumOperations("ab","abbccccc", "abc")
print(output)