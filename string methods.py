Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="twinkle twinkle little star"
a.count("t")
5
a.count(3)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a.count(3)
TypeError: count() argument 1 must be str, not int
a.count(len(a))
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a.count(len(a))
TypeError: count() argument 1 must be str, not int
>>> a.count("star")
1
>>> a=1,2,4,4,5,5,66
>>> a.count(2)
1
>>> a="code"
>>> a.find("code")
0
>>> a="kali krishna"
>>> a.find("kalikrishna")
-1
>>> a.find("kali krishna")
0
>>> a.find("k") + a.find("r")
6
>>> a="name\nmobile\tmailid\nphonenumber"
>>> print(a)
name
mobile	mailid
phonenumber
>>> a="name:kalikrishna\nmobile:2759859345\tmailid:sdsgsfbk@gmail.com\nphonenumber:2985550053"
>>> print(a)
name:kalikrishna
mobile:2759859345	mailid:sdsgsfbk@gmail.com
phonenumber:2985550053
>>> a="name:kalikrishna\nmobile:2759859345\nmailid:sdsgsfbk@gmail.com\nphonenumber:2985550053"
... print(a)
SyntaxError: multiple statements found while compiling a single statement
>>> a="name:kalikrishna\nmobile:2759859345\nmailid:sdsgsfbk@gmail.com\nphonenumber:2985550053"
>>> print(a)
name:kalikrishna
mobile:2759859345
mailid:sdsgsfbk@gmail.com
phonenumber:2985550053
>>> #replace concept
>>> a="kali"
>>> a.replace("kali", "krishna")
'krishna'
