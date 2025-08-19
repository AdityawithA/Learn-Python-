def ispalindrome(s):
    return s == s[::-1]
s = "5555"
ans = ispalindrome(s)
if ans:
    print("yes")
else:
    print("no")    