
lst = [12, 3, 4, 10]
last_n = lst.pop()
lst.insert(0, last_n)
print(lst)

lst = [1]
last_n = lst.pop()
lst.insert(0, last_n)
print(lst)

lst = [12, 3, 4, 10, 8]
last_n = lst.pop()
lst.insert(0, last_n)
print(lst)

lst = []
if lst:
    last_n = lst.pop()
    lst.insert( 0 , last_n)
print(lst)


