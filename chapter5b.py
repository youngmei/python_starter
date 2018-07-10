#chapter5b

###fibonacci
##def fib(n):
##    if n==0 or n==1:
##        return n
##    else:
##        return fib(n-1)+fib(n-2)
##print(fib(15))
##
##
##fib=[1,1]
##while True:
##    x=fib[-2]+fib[-1]
##    if x>10000:
##        break
##    fib.append(x)
##print(fib)
##               


###define lamda
##lambda x:x**2
##lambda x,y=10: 2*x+y
###call
##
##f=lambda x,y=10:2*x+y
##print(f(5))
###just because it is anonymous doesn't mean we cannot give it a name!
##g=lambda:[x**2 for x in range(10)]
##print(g())
### a lambda as a dict value
##d={'null':lambda *args,**kwargs:None}
### a lambda as a keyword argument f in another function
##def func(vals,f=lambda x:sum(x)/len(x)):
##    f(vals)
##
##nums=[8128,6,496,28]
##x=sorted(nums)
##y=sorted(nums,key=lambda x:x%13)
##print(nums,x,y)

# 5.8 generator
##def countdown():
##    yield 3
##    yield 2
##    yield 1
##    yield 'Blast off!'
## #generator
##g=countdown()
##next(g)
##x=next(g)
##print(x)
##y,z=next(g),next(g)
##print(z)
##next(g)

##def countdown():
##    yield 3
##    yield 2
##    yield 1
##    yield 'Blast off!'
##for t in countdown():
##    if isinstance(t,int):
##        message="T-"+str(t)
##    else:
##        message=t
##    print(message)


###define
##def square_plus_one(n):
##    for x in range(n):
##        x2=x*x
##        yield x2+1
###call
##for sp1 in square_plus_one(199):
##    print(sp1)


### define subgenerator
##def yield_all(x):
##    for i in x:
##        yield I
##
### palindrome using yield froms
##def palindrome(x):
##    yield from yield_all(x)
##    yield from yield_all(x[::-1])
##
### The above is equivalent to this full expansion:
##def palindrome_explicit(x):
##    for i in x:
##        yield i
##     for i in x[::-1]:
##        yield i

#5.9  decorator
def null(f):
    """Always return None"""
    return

def identify(f):
    """Return the function"""
    return f

def self_referential(f):
    """Return the decorator."""
    return self_referential

#@null
def nargs(*args,**kwargs):
    return len(args)+len(kwargs)
nargs=null(nargs)
#不懂装饰器的应用

def plus1(f):
    def wrapper(*args,**kwargs):
        return f(*args,**kwargs)+1
    return wrapper

@plus1
def power(base,x):
    return base**x
power(4,2)
print(power(4,2))













