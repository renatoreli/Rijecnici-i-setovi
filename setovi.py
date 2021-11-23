#-----------------------------
tpl =(1,2,3)
lst= [1,2,3]
dict = {"a":1,"b":2,"c":3}
st = {1,2,3}
st12=set((5,4,6,1,2,3,3,3,3)) #uvijek sortira

#print(st12)
#metode
print(st)

st.add(98)
st.add(87)

st.update({98,87,66,54,44})
st.remove(66) #samo jednu vrijednost moze ukloniti

st.discard(87)
print(st)
#%%
a={1,2,3,4,5,13}
a.remove(1) # baca error ako element ne postoji
print(a)
a.discard(1) # ne baca error ako element ne postoji
print(a)


b={2,3,45,6,7,8,21,22}
print(b.issubset(a)) # True, preklapaju se
print(b.issuperset(a))
#%%
b={1,2,3,4,5}
print(b)
b.pop(-1)
print(b)
#%%
print(a | b) #a + b
print(a&b)# a i b
print(a-b) #koji su u a, a nisu u b
print(b-a) # koji su u b, a nisu u a
print(a^b) #zbroj (a-b) (b-a), a|b-a&b

for i in a:
    print(i)

if 88 in a:
    print("je")
else:
    print("nije")

c={2,3,4}
d={2,3}
print(c.issubset(a))
# %%
