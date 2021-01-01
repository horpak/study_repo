# -*- coding: utf-8 -*-
"""
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2 (пересечение).

Результатом должен быть такой список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
config_list1 = command1.split()
vlans_list1 = config_list1[len(config_list1) - 1].split(',')
vlans_set1 = set(vlans_list1)
config_list2 = command2.split()
vlans_list2 = config_list2[len(config_list2) - 1].split(',')
vlans_set2 = set(vlans_list2)
vlans_intersec = vlans_set1.intersection(vlans_set2)
print(list(vlans_intersec))
