Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> print("Program starting.\n")
... 
... word = input("Insert a closed compound word: ")
... 
... # Display word details
... print(f"The word you inserted is '{word}' and in reverse it is '{word[::-1]}'.")
... print(f"The inserted word length is {len(word)}")
... print(f"Last character is '{word[-1]}'\n")
... 
... # Substring selection
... print("Take substring from the inserted word by inserting...")
... start = int(input("1) Starting point: "))
... end = int(input("2) Ending point: "))
... step = int(input("3) Step size: "))
... 
... substring = word[start:end:step]
... 
... print(f"\nThe word '{word}' sliced to the defined substring is '{substring}'.")
