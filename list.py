my_list=[]
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.extend([50, 60, 70])
my_list.pop(-1)
my_list.sort()
value30 = my_list.index(30)
print(my_list)

print(f"The index of 30 in my_list is: {value30}")
