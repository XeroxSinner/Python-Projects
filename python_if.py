num1 = 12
key = False

if num1 == 12:
    if key: 
        print('Num 1 is equal to 12 and they have the key.')
    else:
        print('Num1 is equal to 12 and NO KEY.')
elif num1 < 12:
    print('Num 1 is less than 12')
else:
    print('Num 1 is NOT equal to 12')
    
i = 0
for i in range(10):
    print("{} iteration through the loop.".format(i))
    i += 1

h = 0    
while h < 10:
    print("{} iteration through the loop.".format(h))
    h += 1

name = 'Python'
print(len(name))

for i in enumerate(name):
    print (i)
        


    
