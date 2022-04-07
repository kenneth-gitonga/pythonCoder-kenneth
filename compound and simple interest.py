'''
# Calculating simple and compound interest
# Prompt the user to enter the details required
p=float(input('Enter the principle amount:'))
t=int(input('Enter the time required:'))
r=float(input('Enter the rate:'))
# calculate the simple interest
si=p*t*r/100
# calculate the Amount
A=p*(pow((1+r/100),t))
# calculate the compound interest
ci=A-p
# Get the output
print('Simple Interest is:%.4f'%si)
print('The Total Amount is:%.4f'%A)
print('The Compound Interest is:%.4f'%ci)