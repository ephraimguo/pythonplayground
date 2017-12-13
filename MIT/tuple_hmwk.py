aTup = ('I', 'am', 'a', 'test', 'tuple')
aList = list(aTup)

def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    aList = list(aTup)
    res = []
    for i in range(len(aList)):
        if i % 2 == 0:
            res.append(aList[i])
        else:
            pass
    bTup = tuple(res)
    print(bTup)


oddTuples(aTup)







