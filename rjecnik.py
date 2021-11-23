#tuple zip
a = ("a","b","c","d")
b=(1,2,3)

tp1= zip(a,b)
print(tuple(tp1))
#________________________________________________________________________________
#%%
d = {"ime": "Daniel", "prezime": "Jursik", "godine": 50, "ima_potvrdu": False}
print(d)
print(d["ime"])
print(d.get("ime"))

#metode.
d.update({"ima_potvrdu": True}) #overwrite
print(d)

print(d.setdefault("ime232", "novo_ime")) #dohvatit kljuc ako postoji, ako ne postoji dodijelit ce novi kljuc
print(d)

tp1_keys =("ime", "prezime","godine")
tp1_values = 0

new_dict = d.fromkeys(tp1_keys,tp1_values) # u prazan dict pridruzuje vrijednosti koje smo predali u obliku tupla s kljucevima
print(new_dict)

for key in d:
    print(key, d[key])

#new_dict.popitem()
#print(new_dict)

#new_dict.pop("ime")
#print(new_dict)


#d= d.items()
#print(d)

for key, value in d.items(): # ("ime","daniel")
    print(key,value)
#%%
d123= {}
d12 = dict()
print(d123,d12)
# %%
