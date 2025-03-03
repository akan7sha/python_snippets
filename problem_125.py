s = "A man, a plan, a canal: Panama"
#Output: true
#Explanation: "amanaplanacanalpanama" is a palindrome.
i=0
def pallindrome_validity(s):
        f = s.replace(" ","")
        f  = f.replace(":","")
        f = f.replace(",","")
        f = f.lower()
        print(f)
        while i < len(f)-1:
            if f[i] == f[-i]:
                print("it is palindrome")
                break
            else:
                print("not an palindrome")

pallindrome_validity(s)