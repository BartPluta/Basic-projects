price = input('What is the price of house? ')
print(f'The price of the house is {price} $')
credit = input("Do you have any loan? (Y)es or (N)o ")
job = input("Do you have permanent job? (Y)es or (N)o ")

if credit.upper() == 'N' and job.upper() == 'Y':
    good_credit = True
elif credit.upper() == 'Y' and job.upper() == 'Y':
    good_credit = False
elif credit.upper() == 'N' and job.upper() == 'N':
    print("If you don't have permanent job. You are not able to get mortgage.")
    quit()
else:
    print("Customer has very bad credit score. You are not able to get mortgage.")
    quit()

if good_credit:
    print('The buyer has good credit')
    print('The buyer need to put only 10% of down payment')
    print('Your down payment is ' + str(float(price) * 0.1))
else:
    print('The buyer has bad credit')
    print('The buyer need to put 20% of down payment')
    print('Your down payment is ' + str(float(price) * 0.2) + '$')
