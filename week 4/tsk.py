Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
print("Program starting.\n")
... 
... print("Check multiplicative persistence.")
... num = input("Insert an integer: ")
... 
... steps = 0
... 
... while len(num) > 1:
...     digits = [int(d) for d in num]
...     expression = " * ".join(num)
...     product = 1
...     for d in digits:
...         product *= d
...     print(f"{expression} = {product}")
...     num = str(product)
...     steps += 1
... 
... print("No more steps.\n")
... print(f"This program took {steps} step(s)\n")
... print("Program ending.")
... Program starting.
... 
... Check multiplicative persistence.
... Insert an integer: 277777788888899
... 2 * 7 * 7 * 7 * 7 * 7 * 7 * 8 * 8 * 8 * 8 * 8 * 8 * 9 * 9 = 4996238671872
... 4 * 9 * 9 * 6 * 2 * 3 * 8 * 6 * 7 * 1 * 8 * 7 * 2 = 438939648
... 4 * 3 * 8 * 9 * 3 * 9 * 6 * 4 * 8 = 4478976
... 4 * 4 * 7 * 8 * 9 * 7 * 6 = 338688
... 3 * 3 * 8 * 6 * 8 * 8 = 27648
... 2 * 7 * 6 * 4 * 8 = 2688
... 2 * 6 * 8 * 8 = 768
... 7 * 6 * 8 = 336
... 3 * 3 * 6 = 54
... 5 * 4 = 20
... 2 * 0 = 0
... No more steps.
... 
... This program took 11 step(s)
... 
... Program ending.
