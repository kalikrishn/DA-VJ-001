Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets{}
a={1,2.3,'python', 7+9j, True , False}
type(a)
<class 'set'>
b={5,6,7,8,9}
print{b}
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
b
{5, 6, 7, 8, 9}
b.issubset(a)
False
print(b)
{5, 6, 7, 8, 9}
a.issuperset(b)
False
a.union(b)
{False, 1, 2.3, (7+9j), 5, 6, 7, 8, 9, 'python'}
b.issuperset(a)
False
a.intersection(b)
set()
b.intersection(a)
set()
a.update(4)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.update(4)
TypeError: 'int' object is not iterable
a.update(b)
b
{5, 6, 7, 8, 9}
a={1,2,3,4,5,6,7}
b={8,9,10,11,12}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
a.difference(b)
{1, 2, 3, 4, 5, 6, 7}
b.differnce(a)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    b.differnce(a)
AttributeError: 'set' object has no attribute 'differnce'. Did you mean: 'difference'?
yes
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    yes
NameError: name 'yes' is not defined
b.difference(a)
set()
a={1,2,3}
b={4,5,6}
a.difference(b)
{1, 2, 3}
a.symmetric_difference(b)
{1, 2, 3, 4, 5, 6}
a.intersection_update(b)
a
set()
a
set()
b
{4, 5, 6}
a.difference_update(b)
>>> a
set()
>>> b.difference_update(a)
>>> b
{4, 5, 6}
>>> a.symmetric_difference_update(b)
>>> a
{4, 5, 6}
>>> a.pop()
4
>>> a.remove(5)
>>> a
{6}
>>> a.discard(4)
>>> a
{6}
>>> a.copy()
{6}
>>> a.add(2)
>>> a
{2, 6}
>>> a.clear()
>>> a
set()
>>> a={1,2,3,4,5}
>>> b={3,9,10,11,12}
>>> a.isdisjoint(b)
False
>>> a = [9, 1, 5, 2, 8, 4, 6, 3, 7, 0]
>>> a.sort()
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a.reverse()
>>> a
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> a.sort()
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> b=a.[::2]
SyntaxError: invalid syntax
