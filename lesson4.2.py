lst = [0, 1, 7, 2, 4, 8]
if not lst:
    result = 0
else:
    number = 0
    for i in range(0, len(lst), 2):
        number += lst[i]
    result = number * lst[-1]
print(result)