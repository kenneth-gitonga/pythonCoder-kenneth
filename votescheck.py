
'''
#To check if a person is eligible to vote
nationality=input('Enter your nationality:').lower()
age=int(input('Enter your age:'))
party=input('Enter the party you support:').upper()
print('party supported:',party)
if nationality == 'kenyan' and age >= 18:
    print('Eligible to vote')
else:
    print('Not eligible to vote')

