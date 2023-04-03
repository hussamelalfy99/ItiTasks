creditNum=input("please enter you id card :")

def hideCC_numb(ccNumber):
    return '*' * (len(ccNumber)-4)+ccNumber[-4:]

print (hideCC_numb(creditNum))