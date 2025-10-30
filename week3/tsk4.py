Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # A3_T5 Temperature converter (TEST TASK)
... 
... # Print menu
... print("Menu:")
... print("1. Celsius to Fahrenheit")
... print("2. Fahrenheit to Celsius")
... print("3. Exit")
... 
... # Ask for choice
... choice = input("Your choice: ")
... 
... if choice == "1":
...     celsius = float(input("Enter temperature in Celsius: "))
...     fahrenheit = (celsius * 1.8) + 32
...     print(f"{celsius:.1f} °C = {fahrenheit:.1f} °F")
... elif choice == "2":
...     fahrenheit = float(input("Enter temperature in Fahrenheit: "))
...     celsius = (fahrenheit - 32) / 1.8
...     print(f"{fahrenheit:.1f} °F = {celsius:.1f} °C")
... elif choice == "3":
...     print("Exiting...")
... else:
...     print("Unknown option.")
