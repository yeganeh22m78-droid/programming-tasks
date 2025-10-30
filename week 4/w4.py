Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> print("Program starting.\n")
... 
... word_count = 0
... char_count = 0
... 
... while True:
...     word = input("Insert word (empty stops): ")
...     if word == "":
...         break
...     word_count += 1
...     char_count += len(word)
... 
... print("\nYou inserted:")
... print(f"- {word_count} words")
... print(f"- {char_count} characters")
... 
... print("\nProgram ending.")
... Program starting.
... 
... Insert word (empty stops): Close
... Insert word (empty stops): the
... Insert word (empty stops): loop
... Insert word (empty stops): 
... 
... You inserted:
... - 3 words
... - 12 characters
... 
... Program ending.
