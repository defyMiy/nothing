# setup
dec_num = 3888

# programming
roman_symbol = list()
while dec_num > 999:
    roman_symbol.append('M')
    dec_num -= 1000
if dec_num > 899:
    roman_symbol.append('CM')
    dec_num -= 900
if dec_num > 499:
    roman_symbol.append('D')
    dec_num -= 500
if dec_num > 399:
    roman_symbol.append('CD')
    dec_num -= 400
while dec_num > 99:
    roman_symbol.append('C')
    dec_num -= 100
if dec_num > 89:
    roman_symbol.append('XC')
    dec_num -= 90
if dec_num > 49:
    roman_symbol.append('L')
    dec_num -= 50
if dec_num > 39:
    roman_symbol.append('XL')
    dec_num -= 40
while dec_num > 9:
    roman_symbol.append('X')
    dec_num -= 10
if dec_num == 9:
    roman_symbol.append('IX')
    dec_num -= 9
if dec_num > 4:
    roman_symbol.append('V')
    dec_num -= 5
if dec_num == 4:
    roman_symbol.append('IV')
    dec_num -= 4
while dec_num > 0:
    roman_symbol.append('I')
    dec_num -= 1

roman_num = ''.join(map(str, roman_symbol))
print(roman_num)