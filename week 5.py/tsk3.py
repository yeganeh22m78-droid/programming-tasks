Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def main() -> None:
...     print("program starting.")
...     name = asKName
...     def asKName()-> str:
...         name= input("Insert name:")
...         return name
...     def greetUser(PName)-> None;
...     
SyntaxError: expected ':'
>>> def greetUser(PName)-> None:
...     print(f"Hello{PName})
...           
SyntaxError: unterminated f-string literal (detected at line 2)
>>> return None
SyntaxError: 'return' outside function
>>> print(f"Hello{PName}")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(f"Hello{PName}")
NameError: name 'PName' is not defined
>>> def main() -> None:
...     print("program starting.")
...     Width = askDimension("width")
...     Height= askDimdnsions("height")
