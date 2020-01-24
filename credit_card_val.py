#function for ccredit card validation 
#algorithem used luhn algorithem
def credit_card_vali(card_number):
    #check_number = int(card_number)%10
    sum = 0
    if  not(len(card_number)):
        return 0
    else :
        for digit in range(0,len(card_number)-1):
            sum += int(card_number[digit])
        if int(card_number[-1]) +(sum%10== 0):
            return 1 
        else:
            return 0

print(credit_card_vali(raw_input("enter card no : \t")))
