## Lists
```python
#Put your Code here

liste = [10,"hello",200.3]
liste2 = [3,4,5]
liste+liste2
liste.append('d') #-> hängt hinten an
liste.pop(X)#-> returned Item an X aus der Liste und entfernt es
```
- anders als bei Strings kann man Elemente über den Index ändern
sieht auch [[Listen build ins]]

```python


#nest lists in lists

list1 =[1,2,3, [4,5], [6,7,8]]
print(list1)

```

Zahlenliste generieren
[[Generator build in]]

### __Tupel unpacking__
```python
myList=[(1,2),(3,4),(5,6)(7,8)]
len(myList) #->4

for i in myList:
	print(i)
	
######## TUPEL UNPACKING #######
for (a,b) in myList:
	print(a)
	print(b)

```