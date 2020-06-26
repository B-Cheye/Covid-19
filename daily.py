my_list = [0,2,4,6,8,10,12,14,16,18,20]
new = [my_list[0]]
for a,b in zip(my_list,my_list[1:]):
    new.append(b-a)

print(new)