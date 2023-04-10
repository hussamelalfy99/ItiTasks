<<<<<<< HEAD
creditNum=input("please enter you id card :")

def hideCC_numb(ccNumber):
    return '*' * (len(ccNumber)-4)+ccNumber[-4:]

=======
creditNum=input("please enter you id card :")

def hideCC_numb(ccNumber):
    return '*' * (len(ccNumber)-4)+ccNumber[-4:]

>>>>>>> ced794965d0afaff9895e148a6217fc6c908327f
print (hideCC_numb(creditNum))