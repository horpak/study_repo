# -*- coding: utf-8 -*-
"""
Задание 4.7

Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

mac = "AAAA:BBBB:CCCC"
new_mac=(mac.replace(':',''))

print('{:08b}'.format(int(new_mac[0:2],16)), end='')
print('{:08b}'.format(int(new_mac[2:4],16)), end='')
print('{:08b}'.format(int(new_mac[4:6],16)), end='')
print('{:08b}'.format(int(new_mac[6:8],16)), end='')
print('{:08b}'.format(int(new_mac[8:10],16)), end='')
print('{:08b}'.format(int(new_mac[10:12],16)))
print('101010101010101010111011101110111100110011001100')
