Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="kalikrishna"
a.upper()
'KALIKRISHNA'
a.capitlize(k)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a.capitlize(k)
AttributeError: 'str' object has no attribute 'capitlize'. Did you mean: 'capitalize'?
yes
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    yes
NameError: name 'yes' is not defined
a.capitalize(k)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a.capitalize(k)
NameError: name 'k' is not defined
a.capitalize()
'Kalikrishna'
a.tittle()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a.tittle()
AttributeError: 'str' object has no attribute 'tittle'. Did you mean: 'title'?
a.title()
'Kalikrishna'
a.swapcase()
'KALIKRISHNA'
b="python is easy"
b.swapcase()
'PYTHON IS EASY'
b.title()
'Python Is Easy'\
b.upper()
'PYTHON IS EASY'
b.spilt()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    b.spilt()
AttributeError: 'str' object has no attribute 'spilt'. Did you mean: 'split'?
b.split()
['python', 'is', 'easy']
a=abc123
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a=abc123
NameError: name 'abc123' is not defined
a="abc123"
a.isalnum()
True
a=15
a+=5
print(a)
20
a="python is gooooood"
a.startwith("p")
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.startwith("p")
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
a.startswith("p")
True
a=my_name
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a=my_name
NameError: name 'my_name' is not defined
a=2name
SyntaxError: invalid decimal literal
2name="1"
SyntaxError: invalid decimal literal
my_name="hdkuas"
print("Python".lower())
python
a="python and good"
a.strip()
'python and good'
a="python is good"
a.lower()
'python is good'
a.len(a)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a.len(a)
AttributeError: 'str' object has no attribute 'len'
a.len()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a.len()
AttributeError: 'str' object has no attribute 'len'
print(a.len())
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print(a.len())
AttributeError: 'str' object has no attribute 'len'
print(len(a))
14
a.swapcase()
'PYTHON IS GOOD'
a="python is good"
a.count(a)
1
a.count()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a.count()
TypeError: count expected at least 1 argument, got 0
print(count(a))
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    print(count(a))
NameError: name 'count' is not defined. Did you mean: 'round'?
a="python is course"
b="good in codegnan"
print((a+" "+b).title())
Python Is Course Good In Codegnan
print((a+" "+b).strip())
python is course good in codegnan
print((a+b).strip())
python is coursegood in codegnan
print((a+" "+b).join())
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    print((a+" "+b).join())
TypeError: str.join() takes exactly one argument (0 given)
print((a+" "+b)."".join())
SyntaxError: invalid syntax
print((a+" "+b)"".join())
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print((a,b)"".join())
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(" ".join([a, b]))
python is course good in codegnan
>>> a="motu"
>>> b="pathulu"
>>> print("hello {}{}".format(a,b))
hello motupathulu
>>> print("hello {} {}".format(a,b))
hello motu pathulu
>>> print("hello {} hello {}".format(a,b))
hello motu hello pathulu
>>> a="sweety"
>>> b="cutiee"
>>> print(f"hello {a) {b})
...       
SyntaxError: f-string: unmatched ')'
>>> print(f"hello {a {b})
...       
SyntaxError: f-string: unmatched ')'
>>> print(f"hello {a} {b})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> a="sweety"
... b="cutie"
... print(f"hello {a) {b}")
...       
SyntaxError: multiple statements found while compiling a single statement
>>> a="sweey"
... b="cute"
... print(f"hello {a} {b}")
...       
SyntaxError: multiple statements found while compiling a single statement
>>> a=20
...       
>>> a=20
...       
>>> print(a)
...       
20
>>> a=10
...       
