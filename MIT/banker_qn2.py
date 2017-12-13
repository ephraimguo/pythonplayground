# rate = 0.2/12.0

# balance = 129
# annualInterestRate = 0.25
# monthlyInterestRate = annualInterestRate/12
# pay = 10
# month = 12
# low = balance/month
# high = balance*(1+monthlyInterestRate)**month
#
# p1 = balance - pay
# p2 = (1+monthlyInterestRate)**month
# p3 = (1+monthlyInterestRate)**(month)-1
# bal = (p1*p2 - pay*(p3/monthlyInterestRate))
#
# while bal >= 0:
#     pay = (high+low)/2
#
#
#
#
# print('pay is : %f' % pay)
# print('pay is : %d' % round(pay,-1))

monthlyPaymentRate = 0
init_balance = balance
monthlyInterestRate = annualInterestRate/12

while balance > 0:
    for i in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
    if balance > 0:
        monthlyPaymentRate += 10
        balance = init_balance
    elif balance <= 0:
        break
print('Lowest Payment:', monthlyPaymentRate)