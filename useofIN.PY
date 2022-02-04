'''
#To check if a person is eligible to vote
nationality=input('Enter your Country:').lower()
age=int(input('Enter your age:'))
party=input('Enter the party you support:').upper()
country=['kenya','uganda','tanzania']
print('party supported:',party)
if nationality in country and age >= 18:
    print('Eligible to vote')
else:
    print('Not eligible to vote')

