import math
names = ['zhansan','lisi','wanger']
numbers = list(range(101))
sum = 0
for number in numbers:
    if number < 0:
        print(number)
d = {'michale':1,'jack':2,'susan':3}
d['ad'] = 4
s1 = set([1,2,3])
s2 = set([2,3,4])
a = 'abc'
b = a.replace('a','A')
a = -100
b = 1231232
c = 1232
d = abs
e  = int
def MyFirstHanShu(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if(x>=0):
        return x
    else:
        return -x

def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx,ny
x,y = move(100,100,60,math.pi/6)
print(x,y)
def Empty():
    pass
