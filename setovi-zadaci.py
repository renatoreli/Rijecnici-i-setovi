#1. napravite set sa nekim podacima na dva nacina.

#2. napisite program koji iterira kroz set

#3. napisite program koji dodaje clanove / elemente u set

#4. napisite program koji uklanja elemente iz seta.

#5. napisite program koji uklanja element iz seta samo ako je on prisutan.

#%%

a=set((1,2,3,4,5))
a1={6,7,8,9,10}

for i in a:
    print(i)
a.add(19)
print(a)
a1.remove(8)
print(a1)
a1.discard(6)
print(a)
# %%
#6. iz seta {1, 2, 3, 4, 5} izbacite i ispisite posljednji element.
a={1,2,3,4,5}
a.remove(5)
print(a)
# %%
#7. zadani su setovi {"a", "b", "c"} i {1, 2, 3}. zdruzite dva seta.

a={"a", "b", "c"}
b={1,2,3}
print(a|b)

# %%

#8. zadani su setovi a={"a", "b", "c"} i b={1, 2, 3}. ubacite set a u set b.

a={"a", "b", "c"}
b={1, 2, 3}
b.update(a)
print(b)
#%%
#9 zadani su setovi {"jabuka", "kruska", "orah"} i {"jabuka", "tresnja", "kruska"}. napravite set koji sadrzi samo elemente koji se nalaze u oba seta.

a= {"jabuka", "kruska", "orah"}
b = {"jabuka", "tresnja", "kruska"}
print(a&b)
# %%
#10
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
