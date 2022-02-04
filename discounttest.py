
'''
#To check if discount is eligible to different customers
amount = int(input('Enter a Amount. Ksh:'))
if amount>=1000:
    discount=amount*5/100
    payable=amount-discount
    print('Discount is:',discount)
    print('Amount payable is:',payable)

else:
    print('Not eligible for discount')
