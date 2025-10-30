Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
```python
while True:
...     try:
...         value = int(input("\nInsert an integer value: "))
...     except ValueError:
...         print("Please enter a valid integer.")
...         continue
... 
...     print("\nMenu:")
...     print("1. In one multi-branched decision")
...     print("2. Independent if-statement decisions")
...     print("0. Exit")
...     choice = input("Choose an option: ")
... 
...     if choice == "1":
...         # Multi-branched decision
...         if value >= 400:
...             value += 44
...         elif value >= 200:
...             value += 22
...         elif value >= 100:
...             value += 11
...         print(f"Result: {value}")
... 
...     elif choice == "2":
...         # Independent decisions
...         if value >= 400:
...             value += 44
...         if value >= 200:
...             value += 22
...         if value >= 100:
...             value += 11
...         print(f"Result: {value}")
... 
...     elif choice == "0":
...         print("Exiting...")
...         break
... 
...     else:
...         print("Unknown option.")
... ```
