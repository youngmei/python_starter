#4.3 loop
#4.3.1 while_loop
##t=3
##while t>0:
##    print("t-minus "+str(t))
##    t=t-1
##print("blastoff!")


##x=20
##while x>10:
##    print(x,"I am sorry, Dave.")
##    x=x-1
##print(x,"I cannot print that for you.")


#fibonacci number
##fib=[1,1]
##while True:
##    x=fib[-2]+fib[-1]
##    if x%35==0:
##        break
##    fib.append(x)
##print(fib)
##y={x**2 for x in fib if x%5==0}
##print(sorted(y))


#4.3.2 for_loop

##for t in [3,2,1]:
##    print("t-minus "+str(t))
##print("Blastoff!")


##for t in [7,6,5,4,3,2,1]:
##    if t%2!=0:
##        continue
##    print("t-minus "+str(t))
##print("Blastoff!")


##for letter in "Gorgus":
##    print(letter)



##for letter in {0,"Gorgus",True}:     #change the order, print the same
##    print(letter)



##d={"first":"Albert",
##   "last":"Einstein",
##   "Birthday":[1879, 3,14]}
##for key in d:
##    print(key)
##    print(d[key])
##    print("========")
###the output order is different with that in the textbook
##

####################################################3
##d={"first":"Albert",
##   "last":"Einstein",
##   "Birthday":[1879, 3,14]}
##
##print("Keys:")
##for key in d.keys():
##    print(key)
##print("\n========\n")
##
##print("Values:")
##for value in d.values():
##    print(value)
##print("\n========\n")
##
##print("Items:")
##for key,value in d.items():
##    print(key,value)
#####################################################

##quarks={'up','down','top','bottom','charm','strange'}
##for quark in quarks:
##    print(quark)
##    


#4.3.3 comprehension    
##quarks={'up','down','top','bottom','charm','strange'}
##upper_quarks=[]
##for quark in quarks:
##    upper_quarks.append(quark.upper())
##print(upper_quarks)
##
## list comprehension
##quarks={'up','down','top','bottom','charm','strange'}
##upper_quarks=[quark.upper() for quark in quarks]
##print(upper_quarks)
##

#set comprehension
##entries=['top','CHARm','Top','sTRANGE','TOP']
##quarksa={quark.upper() for quark in entries}
##quarksb={quark.lower() for quark in entries}
##print(quarksa,quarksb)


# dict comprehension
##entries=[1,10,12.5,65,88]
##results={x:x**2+42 for x in entries}
##print(results)


##pm=['Newton','is','the','most','famous','scientist','in','the','human','history']
##t_words=[word for word in pm if word.startswith('t')]
##print(t_words)



coords={'x':1,'y':2,'z':3,'r':1,'theta':2,'phi':3}
polar_keys={'r','theta','phi'}
polar={key:value for key, value in coords.items() if key in polar_keys}
print(polar)
print(coords)































