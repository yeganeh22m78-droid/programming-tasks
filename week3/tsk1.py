Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # A3_T1 If-statements
... 
... # Ask user for two integers
... num1 = int(input("Enter the first integer: "))
... num2 = int(input("Enter the second integer: "))
... 
... # Compare integers
... if num1 == num2:
...     print("Integers are the same.")
... elif num1 > num2:
...     print("First integer is greater.")
... else:
...     print("Second integer is greater.")
... 
... # Calculate sum
... total = num1 + num2
... print("The sum of the two integers is:", total)
... 
... # Check parity
... if total % 2 == 0:
...     print("Sum is even.")
... else:
...     print("Sum is odd.")
