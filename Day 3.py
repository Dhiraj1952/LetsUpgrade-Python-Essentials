#Q1 Pilot programs
print("*******Welcome to Lets upgrade Airways*********")
A=int(input("Enter the current altitude of Plane(in fts):  "))
if A<=1000:
    print("You are safe to land the plane")
elif A<5000:
    print("Please bring down your altitude to 1000 ft.")
else:
    print("********Attention*********")
    print("Your Speed is to high, Please turn around")

#Q2 Prime number

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")