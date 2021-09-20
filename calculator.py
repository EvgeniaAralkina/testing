def fast_mul(a, b):
    k = 1
    # умножение на отрицательное число
    #if (a < 0 and b > 0) or (a > 0 and b < 0):
    #    k = -1
    a = abs(a)
    b = abs(b)
    a1 = [a]
    b1 = [b]
    s = 0
    if a % 2 != 0:
        s += b
    while a > 1:
        if (a // 2) % 2 != 0:
            b1.append(b * 2)
            s += b * 2
        a = a // 2
        b = b * 2

    return s * k


def fast_pow(x, n):
    p = 1
    s = 1
    # возведение в отрицательную степень
    #if n < 0:
    #    p = -1
    #    n = abs(n)
    while n > 0:
        s = fast_mul(s, x)
        n -= 1
    if p == -1:
        return s ** (-1)
    return s

def fast_square_root(a,b):
    return fast_pow(a, b**(-1))

print('Welcome fast multiplication exponentiation!')
while (1):
    print('\nselect:')
    print('1 - fast mul\n2 - fast pow\n3 - fast square root\n')
    x = int(input('   ->'))
    a = int(input('a = '))
    b = int(input('(степень корня) b = '))
    if x == 1:
        print('a * b = ',fast_mul(a,b))
    elif x == 2:
        print('a**b = ',fast_pow(a,b))
    else:
        print('a sqrt b = ', fast_square_root(a,b))

