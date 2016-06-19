"""
Converts a decimal number to any given numeric system and vice versa
"""


# A)
# converts decimal number (number) to other numeric system (sys)
def dec_to_other(number,sys): #number is the decimal number to be converted to the numeric system specified by the parameter sys
    list_of_digits=[]
    while number>0:
        digit=number%sys
        list_of_digits.append(str(digit)) #converted numbers are represented as strings
        number=number//sys
    return "".join(list_of_digits[::-1])


#B)
#string non_dec is the non-decimal number to be converted to decimal, integer sys specifies the numeric system it is to be converted from
def other_to_dec(non_dec,sys): 
    digits=list(non_dec)
    power=len(digits)-1
    decimal=0
    i=0
    while power>=0:
        decimal=decimal+sys**power*int(digits[i])
        i+=1
        power-=1
    return decimal
