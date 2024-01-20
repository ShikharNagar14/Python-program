#  change the value for a different result
num = 7

# To take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
# perfect square

n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")

# # Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")



# # Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

# def isPalindrome(str):
  
#     # Run loop from 0 to len/2
# for i in range(0, int(len(str)/2)):
#         if str[i] != str[len(str)-i-1]:
#             # return False
        # return True
  
# main function
# s = "malayalam"
# ans = isPalindrome(s)
  
# if (ans):
#     print("Yes")
# else:
#     print("No")

#  7

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 7

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))




# 8.

file1 = open('myfile.txt', 'w')
file1.writelines()
file1.close()
 
# Using readlines()
file1 = open('myfile.txt', 'r')
Lines = file1.readlines()
 
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))


# 9.

fo=open("hp.txt","w")
fo.write("Harry Potter")
fo.write("There is a difference in all harry potter books\nWe can see it as harry grows\nthe books were written by J.K rowling ")
fo.close()

fo=open('hp.txt','r')
fi=open('writehp.txt','w')
l=fo.readlines()
for i in l:
    if 'a' in i:
        i=i.replace('a','')
        fi.write(i)
fi.close()
fo.close()


