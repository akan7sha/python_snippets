from Cython import returns

temp_string = "aaabbeeecccaaaaddddeeee"
#print(len(temp_string))
i=0
c = 1
d = ""
for i in range(len(temp_string)-1):
    #print("value of i=",
    if temp_string[i] == temp_string[i+1]:
        c = c+1
        #print(d, c)
    else:
        temp_string[i] != temp_string[i+1]
        d = d.join(temp_string[i])
        print(d, c)
        c = 1
print(temp_string[i], c)


