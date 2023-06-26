def reverse(string):
    string = list(string)
    string.reverse()
    return "".join(string)
s = "Ganesh"
print("The string  is : ", s)
print("reverse string is:",reverse(s))