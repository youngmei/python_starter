#chapter4, practice
###4.1 condition sentence
##h_bar=1.0
##if h_bar==1.0:
###    print("h_bar isn't really unity! Resetting...")
##    h_bar=1.05457173e-34
##pi=3.1415926
##h=2*pi*h_bar
###print(h)


#4.1.1 if-else sentence
##import math
##x=1.0
##if x!=0:
##    y=math.sin(1/x)
##else:
##    y=(x+100)**3
##    y=sqrt(x)
##print(x,y)
##

from math import *
x=0.0
if x!=0:
    y=sin(1/x)
else:
    y=cos(x+100)
print(x,y)


###4.1.2 if-elif-else
##omega=1
##if omega<1.0:
##    signal=0.0
##elif omega>10.0:
##    signal=0.0
##else:
##    signal=1.0
###print(omega,signal)
##
##omega=10.09
##if omega<0.9:
##    signal=0.0
##elif omega>0.9 and omega<1.0:
##    signal=(omega-0.9)/0.1
##elif omega>10 and omega<10.1:
##    signal=(10.1-omega)/0.1
##elif omega>10.1:
##    signal=0.0
##else:
##    signal=1.0
###print(omega,signal)
##
###4.1.3 if-else
##h_bar=1.05457173e-34 if h_bar==1.0 else h_bar
###print(h_bar)

#4.2 try-except
##val=23
##try:
##    inv=1.0/val
##except:
##    print("A bad value was submitted {0}, please try again".format(val))
###print(inv)


##val=0.1
##try:
##    inv=1.0/val
##except ZeroDivisionError:
##    print("A zero value was submitted, please try again")
##except:
##    print("A bad value was submitted {0}, please try again".format(val))
##print(val,inv)

##val=0.0
##if val==0.0:
##    raise ZeroDivisionError("Taking the inverse of zero is forbidden!")
##inv=1.0/val
#print(val,inv)
