# Die Print-Fkt.
## .format()-Methode
Man definiert seinen String 
```python
#put your Code Here
print("String und sein erster {} und sein zweiter {}".format('Platzhalter1', 'Platzhalter2'))
print('the {2} {1} {0}'.format('fox', 'brown', 'quick')) #--> the quick brown fox
print('the {q} {b} {f}'.format(f='fox', b='brown', q='quick'))
```

## f-Strings
```python
name="andi"
print(f'Hi ich bin {name}')

```

## Floating Points formatieren
```python
#{value:width.precision}
result = 100/777
print("The result was {r:1.3f}".format(r=result)) #3 Nachkommastellen

```


## Alignement in Strings
Within the curly braces you can assign field lengths, left/right alignments, rounding parameters and more
```python
print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))

```