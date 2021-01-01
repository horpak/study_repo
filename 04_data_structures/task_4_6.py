# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = "0      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
print(ospf_route)
ospf_route_new = ospf_route.replace('      ',' ')
ospf_route_list = ospf_route_new.split()
print(ospf_route_new)
print(ospf_route_list)
print('{:23} {:23}'.format('Protocol','OSPF'))
print('{:23} {:23}'.format('Prefix', ospf_route_list[1]))
print('{:23} {:23}'.format('AD/Metric', ospf_route_list[2].strip('[]')))
print('{:23} {:23}'.format('Next-Hop', ospf_route_list[4].rstrip(',')))
print('{:23} {:23}'.format('Last update', ospf_route_list[5].rstrip(',')))
print('{:23} {:23}'.format('Outbound Interface', ospf_route_list[6]))
