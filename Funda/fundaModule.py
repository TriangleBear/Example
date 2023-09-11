def assignVar():
    fname = "Kurt"
    x = 100
    y = 100.20

    print(fname)
    print(x)
    print(y)

def mulAssign_1():
    x=y=z=1
    print(x)
    print(y)
    print(z)

def mulAssign_2():
    x,y,z = 1,2,"Kurt"
    print(x)
    print(y)
    print(z)

def dataTypes_num():
    x = int(6)
    y = float(1.2)
    z = complex(3091212.02910)
    print(x)
    print(y)
    print(z)

def dataTypes_str():
    strWrld = 'Welcome to TIP'
    print(strWrld)
    print(strWrld[0])
    print(strWrld[3:4])
    print(strWrld[4:])
    print(strWrld * 8)
    print(strWrld+"Work")

def dataTypes_list():
    list = ['xyz', 684, 4.59, 'kurt zac', 246.5]
    tinylist = [213, 'zac kurt']

    print(list)
    print(list[3])
    print(list[3:4])
    print(list[4:])
    print(tinylist*7)
    print(list+tinylist+tinylist)

def dataTypes_tuples():
    tuple = ('xyz', 684, 4.59, 'kurt zac', 246.5)
    tinytuple = (213, 'zac kurt')

    print(tuple)
    print(tuple[0])
    print(tuple[2:3])
    print(tuple[4:])
    print(tinytuple*6)
    print(tuple+tinytuple+tuple)
    
def dataTypes_dict():
    dict = {}
    dict['probably one'] = "This is one right?"
    dict[2] = "maybe 2, idk"

    tinydict = {'name': 'Kurt', 'code':2001, 'dept': 'BSCS'}

    print(dict['probably one'])
    print(dict[2])
    print(tinydict)
    print(tinydict.keys())
    print(tinydict.values())

def operatorDM_if():
    a = 53
    b = 421
    if b > a:
        print(f'{b} is grater than {a}')

def operatorDM_elif():
    a = 53
    b = 53
    if b > a:
        print(f'{b} is grater than {a}')
    elif a == b:
        print(f'{a} is equal to {b}')

def operatorDM_else():
    a = 421
    b = 53
    if b > a:
        print(f'{b} is grater than {a}')
    elif a == b:
        print(f'{a} is equal to {b}')
    else:
        print(f'{a} is greater than {b}')
