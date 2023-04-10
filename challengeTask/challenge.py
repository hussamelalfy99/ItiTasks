def primeNum():
    file=open("results.txt","w")
    for number in range(1,251):
        if number==3:
            print (str(number)+"is prime")
            file.write(str(number)+"is a prime number\n")
        for prime in range (2,int(number/2+1)):
            if number % prime ==0:
                break
            elif prime== int(number/2):
                print(str(number)+"is prime")
                file.write(str(number)+"is a prime number \n")
    file.close()

primeNum()            
