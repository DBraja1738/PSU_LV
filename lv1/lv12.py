try:
    x=float(input("unesi kvocijent"))
except:
    print("krivi unos")
if x>1 or x<0:
    ("broj je van intervala")

if x>=0.9:
    print("A")
elif x>=0.8:
    print("B")
elif x>=0.7:
    print("C")
elif x>=0.6:
    print("D")
elif x<0.6:
    print("F")