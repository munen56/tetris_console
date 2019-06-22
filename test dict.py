
#dictest = {0: [21], 1: [20, 21, 22]}
dictest = {0: [19,20], 1: [20, 21], 2: [21,22]}

collision_dict = {}

max_key = max(dictest.keys())
min_key = min(dictest.keys())

if len(dictest.keys()) != max_key + 1:
    print("invalid pattern, les piece ne se touche pas")

collision_dict[max_key] = dictest[max_key]
print(collision_dict)

for i in range(1,max_key+1):
    print(i)
    temp_list=[]
    for a in dictest[max_key - i]:
        for b in dictest[max_key]:
            if a != b:
                temp_list.append(a)
                break
        for b in dictest[max_key]:
            if a==b:
                temp_list.remove(a)

    collision_dict[max_key - i] = temp_list

print (collision_dict)

