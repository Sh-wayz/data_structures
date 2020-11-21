import elist
"""
test_list = elist.EnhancedList()

print(test_list)
print(test_list.append('test1'))
print(test_list.append('test2'))
print(test_list.append('test3'))
print(test_list.append('indices test'))
print(test_list.append('indices test'))
print(test_list.indices('indices test'))
print(len(test_list))
print('testing .copy()...')
test_list2 = test_list.copy()
test_list2[0] = 'testing deep copy'
print(test_list)
print(test_list2)"""

elist1 = elist.EnhancedList()

print(elist1)

elist1.append('help')
elist1.append('me')
elist1.append('im')
elist1.append('stuck')
elist1.append('in')
elist1.append('a')
elist1.append('a')
elist1.append('list')
elist1.append('factory')
print(elist1)
print(elist1.append('Haha im just kidding, I am perfectly fine and in excellent health. hah. hah. heh.'))
print(elist1)
print(elist1.indices('a'))
elist2 = elist1.copy()
print(elist2)
print(elist1.indices('a'))
print('\n\n\n\n\n\n\n')
print(type(elist1.indices('a')))
print(type(elist1))
print(elist1.indexes('a'))
