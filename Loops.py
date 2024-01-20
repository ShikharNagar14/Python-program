'''n1=int(input("Enter first number :"))
n2=int(input("Enter second number : "))
product=0
count=n1
while (count>0):
    count=count-1
    product=product+n2
print("the product of two number is ",product)

for row in range(1,11):
    for col in range(1,11):
        prod=row*col
        if prod<10:
            print(prod,end="")
        else:
            print(prod)
print()

# Write a programme to repeatedly ask from user some number until a string is typed and the programme should print the sum of numbered entered bye user
total=0
a=input('enter a number or "done":')
while a!="done":
    num=int(a)
    total=total+num
    a=input('enter a number or "done":')
print("the sum of numbers entered by user ",total)


num=int(input("Enter a number : "))
if num%2==0:
    print("True")
else:
    print("False")
# write A programme that calculates number of seconds in a year
year=int(input("Enter a year: "))
seconds=365*year*24*60*60
print(seconds)'''


# n1=int(input("Enter first number :"))
# n2=int(input("Enter second number :"))
# if (n1%n2==0):
#     print("n1 is divisible by n2")
# else:
#     print("n1 is not divisible by n2")



