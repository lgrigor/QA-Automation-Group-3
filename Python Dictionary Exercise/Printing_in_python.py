'''
1. Print a box like the one below.
a. Using four statement.
b. Using one statement with concatenation.
c. Using one statement
                *******************
                *******************
                *******************
                *******************
'''

print('a] Using four statement.')
print('*'*10)
print('*'*10)
print('*'*10)
print('*'*10)

print('\nb] Using one statement with concatenation.')
print('*'*10 + '\n' + '*'*10 + '\n' + '*'*10 + '\n' + '*'*10)
print()
print(('*'*10 + '\n')*4, end='')

print('\nc] Using one statement')
print('*'*10, '*'*10, '*'*10, '*'*10, sep='\n')

'''
2. Print a box like the one below.
a. Using four statement.
b. Using one statement with concatenation.
c. Using one statement
                *******************
                *                 *
                *                 *
                *******************
'''

print('\na] Using four statement.')
print('*'*10)
print('*' + ' '*8 + '*')
print('*' + ' '*8 + '*')
print('*'*10)

print('\nb] Using one statement with concatenation.')
print('*'*10 + '\n' + '*' + ' '*8 + '*\n' + '*' + ' '*8 + '*\n' + '*'*10)

print('\nc] Using one statement')
print('*'*10, '\n*', ' '*8, '*', '\n*', ' '*8, '*\n', '*'*10, sep='')

'''
3. Print a triangle like the one below.
a. Using four statement.
b. Using one statement with concatenation.
c. Using one statement
                0001000
                0011100
                0111110
                1111111
'''

print('\na] Using four statement.')
print('0001000')
print('0011100')
print('0111110')
print('1111111')

print('\nb] Using one statement with concatenation.')
print('0001000\n' + '0011100\n' + '0111110\n' + '1'*7)

print('\nc] Using one statement')
print('0001000', '0011100', '0111110', '1'*7, sep='\n')
print()
print('0001000\n0011100\n0111110\n1111111')