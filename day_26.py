new_lst = ['caroline', 'keshav', 'elenaor']
lst = [name.upper() for name in new_lst if len(name) < 8 ]
print(lst)