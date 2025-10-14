first_list = [0, 1, 0, 12, 3]
result = [x for x in first_list if x != 0]+[x for x in first_list if x ==0]
print(result)

