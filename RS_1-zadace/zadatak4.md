# Zadatak 4.
```
broj = 0
while broj < 5:
    broj += 2
    print(broj)

```
### U početku "broj" je 0, ali unutar while petlje
### prvo se vrijednost poveća za 2 a onda print-a
### tako da će rezultat biti: 2, 4, 6

```

broj = 0
while broj < 5:
    broj += 1
    print(broj)
    broj -= 1

```
### petlja while je u ovom primjeru bekonačna:
### u početku je "broj" 0, unutar petlje prvo
### poveća vrijednost za 1, onda isprinta vrijednost
### i onda smanji vrijednost za jedan, prije
### sljedećeg prolaza kreoz petlju, tako da nikad
### ne postigne vrijednost 5 i petlja nikad ne završi

```

broj = 10
while broj > 0:
    broj -= 1
    print(broj)
    if broj < 5:
        broj += 2
```
### proble s ovom petljom je što se iz nje
### može izać samo ako je broj manji ili jendak nuli
### što se nikad neće dogoditi
### u početku je "broj" vrijednosti 10
### unutar while petlje vrijednost se svakim prolaskom smanju za 1
### do  vrijednosti 5
### jer uvjet if  dodaje 2 na vrijednost "broja"
### kad mu vrijednost padne ispod 5
### i petlja while nikad ne dođe do uvjeta za izlaz
