wr = open('H://aug.txt''a')
aug= [38,36,31,27,38,24,29,29,30,24,33,27,32,24,36,31,41,30,26,34,26,30,31,26,36,23,31,28,31,32,28]

legnagyobb = aug[0]
for elem in aug:
    if elem > legnagyobb:
        legnagyobb = elem
print(f'{legnagyobb}')

legkisebb = aug[0]
for elem in aug:
    if elem < legkisebb:
        legkisebb = elem
print(f'{legkisebb}')

h = 0

for i in aug:
    if i > 31:
        h += 1
print(f'{h}')

print(f'{aug[19]}')

atlag = sum(aug)/2
print(atlag)

hoingadozas = legnagyobb-legkisebb
print(hoingadozas)
















#Lehet e augusztus havi hóméséklet
#A legnagyobb hóméséklet
#A legkisebb hóméséklet
#Hány alkalommal volt a hőmeséklet 31 fok felett?
#mekkora volt a hómérséklet augusztus 20.-án?
#mekkora volt az átlag hőmérséklet?
#mekkora volt a hőingadoszás?
#Fájl írás