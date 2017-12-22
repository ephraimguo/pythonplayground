# def applyEachTo(L, x):
#     result = []
#     for i in range(len(L)):
#         result.append(L[i](x))
#     return result
#
# def square(a):
#     return a*a
#
# def halve(a):
#     return a/2
#
# def inc(a):
#     return a+1
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd':['donkey','dog','dingo']}

def count(dict_a):
    nums = 0
    for keys in dict_a:
        nums += len(dict_a[keys])
    return nums

a = count(animals)
print(a)
print('*'*30)

def biggest(aDict):
    nums = 0
    res = []
    for keys in aDict:
        if len(aDict[keys]) >= nums:
            nums = len(aDict[keys])
            res.append(keys)
            if len(res) > 1:
                del(res[0])
    return res[0]

b = biggest(animals)
print(b)
