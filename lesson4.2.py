lst = [1, 3, 5]
if not lst:
    result = 0
else:
    number = 0
    for i in range(0, len(lst), 2):
        number += lst[i]
    result = number * lst[-1]
print(result)