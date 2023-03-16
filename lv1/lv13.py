lista = []


while True:
    x=input("upisi broj")
    if x == "done":
        break
    if x.isdigit():
        lista.append(float(x))


print("broj elementa:",len(lista))
print("najveci element:",max(lista))
print("najmanji element:",min(lista))
avg=float(sum(lista)/len(lista))
print("prosjecna vrijednost:",avg)
lista.sort()
print(*lista)