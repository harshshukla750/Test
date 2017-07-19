import random
combination = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
passwd=''
for i in range(6):
    combination_index = random.randrange(62)
    passwd = passwd + combination[combination_index]


print(passwd)

