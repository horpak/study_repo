#/bin/python3
NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
nat_list=NAT.split()
#print(nat_list)
#print(nat_list[7])
nat_list[7]=nat_list[7].replace('Fast','Gigabit')
print(' '.join(nat_list))