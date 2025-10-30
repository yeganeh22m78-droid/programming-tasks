Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> name1= alice
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    name1= alice
NameError: name 'alice' is not defined. Did you mean: 'slice'?
>>> # Ask for the user's name and store it in variable Name
... Name = input("What is your name: ")
... 
... # Print a greeting using the collected Name
