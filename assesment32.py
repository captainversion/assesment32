def reverse(string):
    string = list(string)
    string.reverse()
    return "".join(string)
s = input("enter the string:")
print("The string  is : ", s)
print("reverse string is:",reverse(s))
