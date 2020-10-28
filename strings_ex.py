# You can use the backslash \ within a string for continuation of the string in a new line.
# The new line character is not included in the string.

# find and index methods work the same save that find returns -1 and index throws an exception when no char is found
# remember rfind and rindex
# use count for number of occurrence
# don't forget isalnum

astr = 'Well, not so fast \
        big brother watching'
print(astr)

astr = 'Alls well that, ' \
       'well, ends well'
print(astr)

astr = ('That is, assuming '
        'it really ends')
print(astr)

# slices
abc = 'abcdefghijklmnopqrstuvwxyz'
print(abc[-1:-27:-1])

print("-".join(['a','b','c']))

#strip strips characters at the beginning or end of a sequence
a = 'sicci this is a worthy candidate right'
print(a.strip('scghti'))

# swapcase
print('SwapCase'.swapcase())

# text justify
naw = 'na wa ooo'
print(naw.center(30, '*'))
print(naw.rjust(30,'*'))
print(naw.ljust(30,'*'))

# old formatting style
print(('Discount is %s%%' % 4.500))
print('%+30s' % naw)
print('%-30s' % naw)

w = 'saying'
s0 = 'It goes without {w}'.format(w=w)
s1 = 'It also goes without {0[w]}'.format({'w':w})
s2 = 'Yet, it goes without {0[0]}'.format([w])
print(s0,'\n',s1, '\n',s2,sep='')

print(f'The message is: {s2[:3]} {s1.title()}')
print(f'{w:*^10.2}')


a = [1,2,3]
a.insert(6,10)
print(a)