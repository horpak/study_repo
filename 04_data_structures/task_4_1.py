# -*- coding: utf-8 -*-
"""
Задание 4.1

Используя подготовленную строку nat, получить новую строку, в которой
в имени интерфейса вместо FastEthernet написано GigabitEthernet.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
nat_list=nat.split()
nat_list[7]=nat_list[7].replace('Fast','Gigabit')
nat_gigabit = ' '.join(nat_list)
print(nat_gigabit )
print(nat_list)
