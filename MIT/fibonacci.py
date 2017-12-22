# def fibo(n):
#     if n==1 :
#         return 1
#     if n == 2:
#         return 2
#     else:
#         return fibo(n-2)+fibo(n-1)
#
# a = fibo(35)
# print(a)
# print('*'*30)

#fibonacci by dictionary storage
def fib_efficient(n, d):
    if n in d:
        print('if called %d' %n)
        return d[n]

    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        print('recursion called %d' %n)
        return ans

d = {1:1, 2:2}
print(fib_efficient(35, d))
