## Strings 

```python
a = "I don't do that"
test = "h  a  l  l  o"
#Index	0  1  2  3  4
#revers 0 -4 -3 -2 -1	
#SLICE Syntax: [start:stop:step]
#Escape Sequenzen: \n (new Line) \t (Tab)
#String Länge
len(test)
```

### __indexing__ & __slicing__ 
```python
mystr = "Hello World"
len(mystr)
mystr[0] #--> 'H'
mystr[-2]#-->'l' -1 ist immer der letzte Buchstabe des Strings
mystr1='abCdefghijk'
mystr1[2:] #-->von C bis Ende: cdefghijk
mystr1[:3] #-->von Start bis index 3 (aber OHNE include): abc
mystr1[3:6]#-->von index 3 (mint Include) bis index 6 (ohne Include): def

####
mystr1[::2] #-->von Start bis Ende in 2er Schritten
mystr1[2:7:2]#-->Kombination aus Start, Ende & Stepsize
mystr1[::-1]#--> reverse a String
```

### __String Eigenschaften und Methoden__
```python
#Strings lassen sich in PYthon nicht, wie ein Arry in JAVA verändern!
#Beispiel:
str="Sam"
last_letters= str[1:] #-->Output: 'am'
str = 'P'+last_letters
letter = 'x'
letter * 10
````

### Funktionen für Strings 
[[String objs build ins]]


