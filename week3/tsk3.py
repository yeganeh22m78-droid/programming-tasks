Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # A3_T4 More menu options
... 
... # Prompt username
... username = input("Enter your name: ")
... 
... # Print menu
... print("\nMenu:")
... print("1. Print welcome message")
... print("2. Exit")
... print("3. Print the name backwards")
... print("4. Print the first character")
... print("5. Show the amount of characters in the name")
... 
... # Ask for choice
... choice = input("Your choice: ")
... 
... # Perform action
... if choice == "1":
...     print(f"Welcome {username}!")
... elif choice == "2":
...     print("Exiting...")
... elif choice == "3":
...     print(f'Your name backwards is "{username[::-1]}"')
... elif choice == "4":
...     print(f'The first character in name "{username}" is "{username[0]}"')
... elif choice == "5":
...     print(f'There are {len(username)} characters in the name "{username}"')
... else:
...     print("Unknown option.")
