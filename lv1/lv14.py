line_r=[]
brojevi = []

fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        line_r = line.rsplit()
        brojevi.append(float(line_r[1]))
        print(line)
print(sum(brojevi))
print("prosjek je :",sum(brojevi)/len(brojevi))        
fhand.close()