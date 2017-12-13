def debt_qn(balance, ann_ins_rate, min_mth_payrate):
    bal_de_rate = 1 - min_mth_payrate
    mth = 0
    count = 0
    while mth < 12:
        count +=1
        print(count)
        balance = (1+(ann_ins_rate/12))*bal_de_rate*balance
        print(balance)
        mth+=1

    print('*'*30)
    # balance = round(balance, 2)
    print('Remaining balance: %.2f' % balance)
    #print(round(balance, 2))
    return round(balance, 2)

print(debt_qn(5000, 0.18, 0.02))