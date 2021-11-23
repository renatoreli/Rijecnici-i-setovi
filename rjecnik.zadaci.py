#%%
#1. napravite dva prazna rjecnika dictionary1 i dictionary2 (na oba nacina) i jedan rjecnik popunjen proizvoljnim parovima (min. 3). iz treceg rjecnika napravite sljedece:
#    a) ispisite sve kljuceve
#   b) ispisite sve vrijednosti
#    c) ispisite vrijednost nekog kljuca
#    d) ispisite tuple svih kljuceva u rjecniku
dictionary1 = {"ime": "Renato", "Prezime": "Jozinovic", "Spol": "M" }
dictionary2 = dict({"godine":22,"ima_racunalo": True, "potvrda": True })

print("Keys", dictionary1.keys())
print("Values",dictionary2.values())
print("Vrijednost kljuca ",dictionary2.get("godine"))
for key in dictionary2:
    print(key)
# %%
#2. zadani su kljucevi "team1", "team2", "team3". koristeci funkciju fromkeys, pridruzite kljucevima vrijednost 0.
empty_dict={}
d_keys=("team1","team2","team3")
d_values= 0
newdict = empty_dict.fromkeys(d_keys,d_values)
print(newdict)


# %%
#3. zadan je rjecnik {"ime": "pero", prezime: "perkovic", godine: 42}.
# koristeci metodu update, izmijenite vrijednosti rjecnika u vlastito ime, prezime i godine, zatim dodajte novi par "spol" sa prikladnom vrijednosti.

d = {"ime": "pero", "prezime": "perkovic", "godine": 42}
d.update({"ime":"Renato","prezime": "Jozinovic","godine": 22 })
print(d)
d.update({"spol":"M"})
print(d)

# %%
#4 koristeci funkciju setdefault(), dohvatite i ispisite ime i prezime iz prethodnog zadatka. koristeci istu funkciju, kreirajte novi par "visina" i pridruzite prikladnu vrijednost.

d = {"ime": "pero", "prezime": "perkovic", "godine": 42}
print(d.setdefault("ime"))
print(d.setdefault("prezime"))
print(d.setdefault("visina","192"))
print(d)

# %%
#5 kopirajte rjecnik iz prethodnog zadatka, uklonite posljednji unos, a zatim uklonite "spol". ispisite rjecnik.
d = {"ime": "pero", "prezime": "perkovic", "godine": 42, "spol":"M"}
d.popitem()
print(d)
d.pop("spol")
print(d)
# %%
#6. koristeci for petlju, ispisite rjecnik (oba nacina)

d = {"ime": "pero", "prezime": "perkovic", "godine": 42, "spol":"M"}

for key, value in d.items():
    print(key,value)

for key,value in d:
    print(f"kljuc {key} ima vrijednost {d[value]}")
# %%
#7. napravite program koji konkatenira (spaja) tri zadana rjecnika u jedan. 

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
merg={**dic1,**dic2,**dic3}
print(merg)

# %%
#8. napisi program koji provjerava postoji li neki kljuc u rjecniku
d = {"ime": "pero", "prezime": "perkovic", "godine": 42, "spol":"M"}
print(d.setdefault("spol"))

# %%
#9. napisi funkciju koja prima rjecnik te ispisuje sadrzaj rjecnika preko for petlje

d = {"ime": "pero", "prezime": "perkovic", "godine": 42, "spol":"M"}

def dict(d):
    print(d)
dict(d)

for key,value in d.items():
    print(key,value)


# %%
# 12. napisite funkciju koja zbraja sve vrijednosti unutar rjecnika {"1": 1, "2": 2, "3": 3, "4": 4}

d= {"1": 1, "2": 2, "3": 3, "4": 4}
sum(d.values())
# %%
#13. zadan je rjecnik {'data1':100,'data2':-54,'data3':247}. napisi program koji mnozi sve vrijednosti u njemu.

d= {'data1':100,'data2':-54,'data3':247}

answer = 1
for i in d:
    answer = answer*d[i]
print(answer)

# %%
#15. napisi rjecnik sa proizvoljnim vrijednostima i neka sadrzi duplikate. napisi program koji bi uklonio sve parove koji sadrze duplikate.

d = [{"C#" : 1}, {"Rust" : 2}, {"C++" : 3}, {"Rust" : 2}, {"python" : 4},{"python" :4}]

result = []
for i in range(len(d)):
    if d[i] not in d[i+1:]:
        result.append(d[i])
print(result)
# %%
#18. zadan je rjecnik:
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'tinder'],
    'backpack' : ['house key','dagger', 'bedroll','bread loaf']
}
#   a) uklonite dagger iz backpack-a
#  b) uvecajte gold za 50
#    c) uklonite flint i tinder iz pouch i dodajte flint&tinder
#   d) kreirajte pocket te smjestite gold i house key u njeg
print(inventory)
inventory.pop['backpack'][1]
print(inventory)

# %%
#10
n=int(input("upisi broj "))
d={}
def funk(d):
    for x in range(1,n+1):
        d[x]=x*x
    print(d)

funk(d)
# %%
