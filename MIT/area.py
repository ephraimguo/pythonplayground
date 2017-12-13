import math
def polysum(n, s):
    if n == 1 or n == 2:
        print('the number of sides are not enough for a polygon')
    else:
        return round(((0.25*n*(s**2))/(math.tan(math.pi/n)) + (n*s)**2), 4)

