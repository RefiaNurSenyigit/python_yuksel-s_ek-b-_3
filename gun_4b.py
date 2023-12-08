number=int(input("Please enter a number: "))
if 1<=number<=20:
    for i in range(number):
        result=i**2
        print(result)
else:
    print("Please enter a number between 1 to 20")