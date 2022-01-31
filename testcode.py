mySentence = 'loves the color'

color_list = ['black','silver','purple','pink','mint']

name = ['Ny','Sera','Remi','Ellis']

def color_function(name):
    lst = []
    for i in color_list:
        msg = "{} {} {}.".format(name,mySentence,i)
        lst.append(msg)
    return lst 

lst = color_function('I')
for i in lst:
    print(i)

def get_name():
    go = True
    while go:
        name = input('What is your name? ')
        if name == '':
            print('You need to provide a name.')
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)

        
get_name('John')



