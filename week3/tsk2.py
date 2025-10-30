Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # A3_T3 Menu program
... 
... # Prompt username
... username = input("Enter your name: ")
... 
... # Print menu
... print("\nMenu:")
... print("1. Print welcome message")
... print("2. Exit")
... 
... # Ask for choice
... choice = input("Your choice: ")
... 
... # Perform action
... if choice == "1":
...     print(f"Welcome {username}!")
... elif choice == "2":
...     print("Exiting...")
... else:
...     print("Unknown option.")
