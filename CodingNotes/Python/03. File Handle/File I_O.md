# File Handling
```python

myfile = open('test.txt')  
print(myfile.read())  
myfile.seek(0)  
print(myfile.readlines())
#-> gibt die einzelnen Zeilen in einer List zurück
```
- beide read-Methoden haben \n  am Ende der Zeile
- [[Lists]]

```python
with open("../school/scripte/courses\_out.csv") as myCSV:  
    content = myCSV.read()  
    print(content)  
    myCSV.close()
	
```
![[Bildschirmfoto 2021-03-19 um 23.40.24.png]]