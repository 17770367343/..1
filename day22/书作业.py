def func1(num):
    '''接受一个数字为参数并返回它的平方值'''
    return num*num

def func2(s):
    '''接受一个字符串参数并将它打印出来'''
    print(s)

def func3(a,b,c,d=0,e=0):
    '''接受3个必选参数和2个可选参数'''
    print(f'''
    第一个必选参数是{a}，
    第二个必选参数是{b}，
    第三个必选参数是{c}，
    第一个可选参数是{d}，
    第二个可选参数是{e}
    ''')

def func4(num):
    '''接受一个整数并返回它除以2的值'''
    return num/2

def func5(num):
    '''接受一个整数并返回它乘以4的值'''
    return num*4

def func6(num):
    '''调用func4并将其返回值当做参数传给func5'''
    num = func4(num)
    return func5(num)

def func7(s):
    '''接受一个字符串，打印它的每个字符'''
    for i in s:
        print(i)

def func8(s,b):
    '''接受一个字符串，将其按照b字符分割并保留b字符'''
    ls = s.split(b)
    ls2 = []
    for i in ls[:-1]:
        i += b
        ls2.append(i)
    return ls2

s = 'abcbnbvb'
ls = s.split(sep='b')
S=s.capitalize()
print(S)
print(ls)
print(func8(s,'b'))