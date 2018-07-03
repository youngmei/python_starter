#learn section6, chaper 2, EFFECTIVE COMPUTATION INPHYSICS
#STRING
#strings can be connected together.
a="kilo"+"meter"
b="x^"+str(3)
c="python "*3
d="H+H"" ->H2"
#long string can be written in more than one lines. Python neglect the linefeed.
quote=("Science is what we understand well enough to explain to a computer. "
       "Art is everything else we do.""-Donald Knuth")
#single quote marks and double quotation marks, one and the other
x="It\'s easy!" 
y='The computer says, \"I cannot computer it.\"'
z="Bones said, \"He\'s dead, Jim.\""
#I don't know how to print the following sentences.How to use the linefeed here?
e="""Humpy, he sat on a wall,
Then happy, he had a great fall.
But all the king's horses And men with their forces
Couldn't render his entropy small.
"""
#methods
m1="strip(),""upper(),""lower(),""swapcase(),""isdigit(),""format()"
header="   Temperature Pressure \t Value \n"
h1=header.strip()
h2=header.upper()
h3=header.swapcase()
d="10"
d1=d.isdigit()
d2="10.10".isdigit()
f1="{0} gets into work & then his {1} begins!".format("Hilbert","commute")

f2="{0} gets into work & then his {1} begins!".format("Hilbert","commute")*2  #how to use linefeed?

