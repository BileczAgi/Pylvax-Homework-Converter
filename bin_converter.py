"""
Assignment:
Write two functions: 
 A) one which converts decimal numbers to binary and 
 B) one which converts from binary numbers to decimal. 
Represent decimal numbers as integers and binary numbers as strings.
"""
# A)
def dec_to_bin(number): #number is the decimal number to be converted to binary
    list_of_digits=[]
    while number>0:
        digit=number%2
        list_of_digits.append(str(digit)) #binary numbers represented as strings
        number=number//2
    return "".join(list_of_digits[::-1])


#B)
def bin_to_dec(binary):
    digits=list(binary)
    power=len(digits)-1
    decimal=0
    i=0
    while power>=0:
        decimal=decimal+2**power*int(digits[i])
        i+=1
        power-=1
    return decimal


