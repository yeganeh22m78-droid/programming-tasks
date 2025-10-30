Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
```python
def meters_to_kilometers(meters):
    return meters * 0.001  # 1 m = 0.001 km

def kilometers_to_meters(km):
    return km * 1000.0  # 1 km = 1000 m

def grams_to_pounds(grams):
    return grams * 0.00220462  # 1 g = 0.00220462 lb

def pounds_to_grams(pounds):
    return pounds * 453.592  # 1 lb = 453.592 g

while True:
    print("\nMenu:")
    print("1. Length")
    print("2. Weight")
...     print("3. Exit")
...     choice = input("Choose an option: ")
... 
...     if choice == "1":
...         print("\nLength Conversions:")
...         print("1. Meters to Kilometers")
...         print("2. Kilometers to Meters")
...         sub_choice = input("Choose an option: ")
... 
...         if sub_choice == "1":
...             val = float(input("Enter meters: "))
...             print(f"{val} m = {round(meters_to_kilometers(val), 1)} km")
...         elif sub_choice == "2":
...             val = float(input("Enter kilometers: "))
...             print(f"{val} km = {round(kilometers_to_meters(val), 1)} m")
...         else:
...             print("Unknown option.")
... 
...     elif choice == "2":
...         print("\nWeight Conversions:")
...         print("1. Grams to Pounds")
...         print("2. Pounds to Grams")
...         sub_choice = input("Choose an option: ")
... 
...         if sub_choice == "1":
...             val = float(input("Enter grams: "))
...             print(f"{val} g = {round(grams_to_pounds(val), 1)} lb")
...         elif sub_choice == "2":
...             val = float(input("Enter pounds: "))
...             print(f"{val} lb = {round(pounds_to_grams(val), 1)} g")
...         else:
...             print("Unknown option.")
... 
...     elif choice == "3":
...         print("Exiting...")
...         break
...     else:
...         print("Unknown option.")
... ```
