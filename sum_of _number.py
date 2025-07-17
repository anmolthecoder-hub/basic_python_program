n=int(input("enter a number to find the sum of digits:"))
number=0
digit=0
while n>0:
    digit = n % 10
    number=digit+number
    n = n // 10
print("The sum of digits is:", number)