<<<<<<< HEAD
def CountVowelInword(word):
    numOfa =0
    numOfe =0
    numOfi =0
    numOfo =0
    numOfu =0
    for i in word :
        if (i=='a'):
          numOfa+=1
        elif(i=='e'):
          numOfe+=1
        elif(i=='i'):
            numOfi+=1
        elif(i=='o'):
            numOfo+=1
        elif(i=='u'):
             numOfu+=1
    return f' num of a {numOfa}\nnum of e {numOfe}\nnum of i {numOfi}\nnum of o {numOfo}\nnum of u {numOfu}'
inputWord=input("enter the word you want to check:").lower()

=======
def CountVowelInword(word):
    numOfa =0
    numOfe =0
    numOfi =0
    numOfo =0
    numOfu =0
    for i in word :
        if (i=='a'):
          numOfa+=1
        elif(i=='e'):
          numOfe+=1
        elif(i=='i'):
            numOfi+=1
        elif(i=='o'):
            numOfo+=1
        elif(i=='u'):
             numOfu+=1
    return f' num of a {numOfa}\nnum of e {numOfe}\nnum of i {numOfi}\nnum of o {numOfo}\nnum of u {numOfu}'
inputWord=input("enter the word you want to check:").lower()

>>>>>>> ced794965d0afaff9895e148a6217fc6c908327f
print (CountVowelInword(inputWord))