balance = 5000
annualInterestRate = 0.2

init_balance = balance
monthlyInterestRate = annualInterestRate/12
lower = init_balance/12
upper = (init_balance * (1 + monthlyInterestRate)**12)/12.0
epsilon = 0.03
monthlyPaymentRate  = 0

while abs(balance) > epsilon:
    monthlyPaymentRate = (lower + upper) / 2
    balance = init_balance
    print('***')
    for i in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
    if balance > epsilon :
        lower = monthlyPaymentRate
        # balance = init_balance
        # monthlyPaymentRate += epsilon
        # monthlyPaymentRate = (lower+upper)/2
    elif balance < -epsilon:
        upper = monthlyPaymentRate
        # balance = init_balance
        # monthlyPaymentRate+= epsilon

    else:
        break
print('Lowest Payment:', round(monthlyPaymentRate, 2))