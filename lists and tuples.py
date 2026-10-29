Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list
a=[2,3.5,"python",8+9j,True,False]
a.append("maths")
a
[2, 3.5, 'python', (8+9j), True, False, 'maths']
a.append("ml","cse")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a.append("ml","cse")
TypeError: list.append() takes exactly one argument (2 given)
a.append(['physics', 'ece'])
a
[2, 3.5, 'python', (8+9j), True, False, 'maths', ['physics', 'ece']]
a.extend('physics', 'ece')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.extend('physics', 'ece')
TypeError: list.extend() takes exactly one argument (2 given)
a.extend(['extend', 'ece'])
a
[2, 3.5, 'python', (8+9j), True, False, 'maths', ['physics', 'ece'], 'extend', 'ece']
b=['python','maths']
b.extend('cse','chmei')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    b.extend('cse','chmei')
TypeError: list.extend() takes exactly one argument (2 given)
b.extend(['hec','ns'])
b
['python', 'maths', 'hec', 'ns']
b.insert('white')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    b.insert('white')
TypeError: insert expected 2 arguments, got 1
b.insert(1,'mec')
b
['python', 'mec', 'maths', 'hec', 'ns']
b.remove(1,'mec')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    b.remove(1,'mec')
TypeError: list.remove() takes exactly one argument (2 given)
b.remove(1)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    b.remove(1)
ValueError: list.remove(x): x not in list
b.remove('mec')
b
['python', 'maths', 'hec', 'ns']
a=["apple",'banana']
a.index(1)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.index(1)
ValueError: list.index(x): x not in list
a.index('apple')
0
a.pop()
'banana'
a
['apple']
a.pop()
'apple'
a
[]
b=a
b.insert(0,'jack')
b
['jack']
b.remove(0)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    b.remove(0)
ValueError: list.remove(x): x not in list
b.remove('jack')
b
[]
b.insert('vza','mng')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    b.insert('vza','mng')
TypeError: 'str' object cannot be interpreted as an integer
b.insert(0,'vza')
b
['vza']
b.insert(1,'mng')
b
['vza', 'mng']
b.remove(1)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    b.remove(1)
ValueError: list.remove(x): x not in list
b.remove([1])
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    b.remove([1])
ValueError: list.remove(x): x not in list
b.remove(0:1)
SyntaxError: invalid syntax
b=[-1,0,2,3,5,6,7,2]
b.sort()
b
[-1, 0, 2, 2, 3, 5, 6, 7]
a=[1,2,3,4,5]
a.remove([0:2])
SyntaxError: invalid syntax
a=1
b=2.5
a.float()
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a.float()
AttributeError: 'int' object has no attribute 'float'
a.float(b)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a.float(b)
AttributeError: 'int' object has no attribute 'float'
a=float(b)
a
2.5
a=['java','maths']
a.split()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a.split()
AttributeError: 'list' object has no attribute 'split'
>>> print(a)
['java', 'maths']
>>> a.len('java')
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a.len('java')
AttributeError: 'list' object has no attribute 'len'
>>> len(a)
2
>>> len('java')
4
>>> a.count('java')
1
>>> a = [1, 2, 3, (4, 6)]
>>> a.extend(7,8)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a.extend(7,8)
TypeError: list.extend() takes exactly one argument (2 given)
>>> a.extend(7)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a.extend(7)
TypeError: 'int' object is not iterable
>>> a.extend([7,8])
>>> a
[1, 2, 3, (4, 6), 7, 8]
>>> a=1
>>> b=2
>>> c=a*b
>>> print(f'product is {c})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f'product is {c}')
...       
product is 2
