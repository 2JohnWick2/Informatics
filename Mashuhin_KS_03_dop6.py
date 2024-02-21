'''
And so on, from aa to az, then from ba to bz, etc, until zz. The letters before and including trillion should be uppercase, letters after quadrillion should be lowercase to easy distinguish between the 'common' notation and 'aa' one.

Your task
Your task is to write a function that accepts a floating point number and formats it using the notation given above.

The resulting number should include 3 most significant digits and be rounded down towards zero (for example, 1238 should be 1.23K, and -1238should be -1.23K). All trailing zeroes after the decimal point should be removed, and the decimal point should be excluded if the resulting number is whole number of units after the rounding down. If the number is too small and it's rounded down to 0, then 0 should be returned. Beware of the negative zero, which should not appear in the output, instead the regular zero 0 should be returned.

Input limitation
The input is a finite floating point number in range -103 < x < 103.
'''

import string


alphabet = list(string.ascii_lowercase)
numor = int(input('Введите ваше число: '))
if numor >= 0:
    min = ''
else:
    min = '-'
numor = abs(numor)
num = numor
pow = -1
while num > 0:
    pow += 1
    num //= 10
cutnumor = round(numor/10**((pow//3)*3), 2)


def monalfa(pow):
    abcpowmon = (pow-15)//78
    if pow-15 >= 0:
        mon = alphabet[abcpowmon]
    else:
        mon = ''
    return (mon)


def secalfa(pow):
    abcpowsec = ((pow-15) % 78)//3
    if pow-15 >= 0:
        sec = alphabet[abcpowsec]
    else:
        sec = ''
    return sec


def belfif(pow):
    if pow < 3 or pow >= 15:
        bel = ''
    if 6 > pow >= 3:
        bel = 'K'
    if 9 > pow >= 6:
        bel = 'M'
    if 12 > pow >= 9:
        bel = 'B'
    if 15 > pow >= 12:
        bel = 'T'
    return bel


if -(10**303) <= numor <= (10**303):
    print(min, cutnumor, monalfa(pow), secalfa(pow), belfif(pow), sep='')
else:
    print('TOO MUCH')
