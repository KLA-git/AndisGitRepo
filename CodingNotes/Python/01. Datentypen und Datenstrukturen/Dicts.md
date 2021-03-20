## Dictionaries
```python
#Put your Code here
dicts={
"mapKey": "wert",
"name": "Frank",
}
dicts["name"]
```
- ungeordnete "KEY":"VAL" - Paare
- call Key -> return Value
- ungeordnet, können nicht sortiert werden
- dicts können auch anderen dicts oder listen enthalten

```python
#Key: Val paare zu Dicts adden
dicts={
"mapKey": "wert",
"name": "Frank",
}

dicts["alter"] =36
```

### Iterieren DICTIONARIES
```python
myD={
	'k1':1,
	'k2':2,
	'k3':3,
	}
for item in myD:
	print(item) #-> man kommt nur an Keys

for item in myD.items():
	print(item)#-> Tupel unpacking der Ausgabe:

######## TUPEL UNPACKING #######
for key,value in myD.items(): 
	print(value)
	print(key)
	


```
[[Dictionaries build ins]]