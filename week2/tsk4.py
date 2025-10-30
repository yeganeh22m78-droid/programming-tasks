Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> print("Program starting.")
... print("Estimate how many minutes you spent on programming...\n")
... 
... times = []
... for i in range(1, 8):
...     t = int(input(f"A1_T{i}: "))
...     times.append(t)
... 
... total = sum(times)
... avg = total / len(times)
... 
... print(f"\nIn total you spent {total} minutes on programming.")
... print(f"Average per task was {avg:.2f} min and same rounded to the nearest integer {round(avg)} min.")
... 
