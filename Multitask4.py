inputString = input("enter your string :")
def double_char(stringTobeDoubled):
    return ''.join([char*2 for char in stringTobeDoubled])

print (double_char(inputString))
