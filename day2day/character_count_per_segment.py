from Cython import returns

temp_string = "aabbbaccdddd"
#print(len(temp_string))
c = 1
for i in range(0, len(temp_string)-1):
    #print("value of i=", i)
    if temp_string[i] == temp_string[i+1]:
        c = c+1
    else:
        print(temp_string[i], c)
        c = 1



