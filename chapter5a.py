#chapter5 functions


#5.1 function in python
##def sagan():
##    quote="With insufficient data it is easy to go wrong."
##    return quote
##print(sagan())
###define a function doesn't return any output,
###return a value, then the function has an output 
##
##
##def null():
##    pass
##
###define the function
##def forty_two():
##    return 42
##
###call the function
##forty_two()
##
###call the function, and print the result
##print(forty_two())
##
###call the function, assign the result to x, and print x
##x=forty_two()
##y=sagan()
##print(x,"\n",y)


###define the function
##def forty_two_or_bust(x):
##    if x:
##        print(42)
##    else:
##        print(0)
###call the function
##forty_two_or_bust(True)
##bust=False
##forty_two_or_bust(bust)


###define
##def power(base,x):
##    """Computer base^x. Both base and x should be integers, floats, or another numeric type."""
##    return base**x
###call
##y=power(3,12)
##print(y)


###define function
###使用数学函数之前，先要输入
##from math import sin
##def sin_inv_x(x):
##    if x==0:
##        result=0.0
##    else:
##        result=sin(1.0/x)
##    return result
###call
##y=sin_inv_x(0.3)
##print(y)


##def line(x,a=1.0,b=0.5):
##    return a*x+b
##y=line(42,b=2,a=1)
##print(y)


##def myappend(x,lyst=None):
##    if lyst is None:
##        lyst=[]
##    lyst.append(x)
##    print(lyst)
##    return lyst
##myappend(12,[])


###define
##def minimum(*args):
##    """Takes any number of arguments!"""
##    m=args[0]
##    for x in args[1:]:
##        if x<m:
##            m=x
##    return m
###return 必须与 for 对齐，才能实现多次比较，从而得到最小的数。
###如果 return 与 if 对齐，则只比较一次，得到较小的数。
###call
##m1=minimum(7,6,2,30)
##print(m1)
##data=[65,42,200,8]
##y=minimum(*data)
##print(y)


###define
##def blender(*args,**kwargs):
##    """Will it?"""
##    print(args,kwargs)
###call
##blender("yes",43)
##blender(z=6,x=32)
##blender('no',[1],'yes',z=4,x=32)
##
##t=('no',)
##d={'mom':'ionic'}
##blender("yes",kid="covalent",*t,**d)


###define function
##def momentum_energy(m,v):
##    p=m*v
##    e=0.5*m*v**2
##    return p,e
###call function
##p_e=momentum_energy(30,30)
##print(p_e)
###p_e返回两个值
##
##mom,eng=momentum_energy(30,30)
##print(mom)
##print(eng)


###global scope
##a=6
##b=42
##def func(x,y):
##    #local scope
##    z=16
##    return a*x+b*y+z
###global scope
##c=func(1,5)


###global scope
##a=6
##b=42
##def outer(m,n):
##    #outer's scope
##    p=10
##    def inner(x,y):
##        #inner's scope
##        return a*p*x+b*n*y
##    #outer's scope
##    return inner(m+1,n+1)
###global scope
##c=outer(1,5)
    

##a=6
##def a_global():
##    print(a)
##def a_local():
##    a=42
##    print(a)
##a_global
##a_local
##print(a)


a="A"

def func():
    #you cannot use the global 'a' because...
    print("Big "+a)
    #A local 'a' is eventually defined!
    a="a"
    print("small "+a)
    
func()


















