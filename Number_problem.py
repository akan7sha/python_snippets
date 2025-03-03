from Cython import returns

a = [1,2,5,6,9]

for i in range(len(a)):
    #print(a[i])
    d = ''.join(map(str, a))
    e = int(d)+ 1

print(list(str(e)))


