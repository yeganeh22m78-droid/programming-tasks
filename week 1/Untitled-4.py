def is-prime(num):
if num <=1:
    return False
for i in range(2,int(num**0.5+1)):
if num % i == 0:
    return False
return True
while True:
    number = int(input("Enter a number"))
    if is-prime(number):
        print(f"{number}is a prime number")
    else:
        print(f"{number}is not a prime number")
        again = input("Do you want to test another number?(y/n):").lower()
        print("program ended.")
        break