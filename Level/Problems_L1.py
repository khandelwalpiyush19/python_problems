# Develop a program for multiplication table of a particular number

# number = int (input("Enter a number : "))
# i=1
# while i <=10:
#     print(f"{number} x {i} = {number * i}")
#     i+=1

# =========================================================================================

# create a program to sum all odd numbers upto a given number

# number = int(input("Enter a Number: "))
# sum_odd = 0

# for i in range(1, number + 1, 2):   
#     sum_odd += i  

# print(f"The sum of all odd numbers up to {number} is {sum_odd}")

# =========================================================================================

# write a program that calculates factorial of a given number

# number = int(input("Enter a  number : "))
# factorial = 1
# for i in range(1,number+1):
#     factorial *= i
# print(f"the factorial fo {number} is {factorial}")

# =========================================================================================

# write a program to calculate the sum of digtis of an integer

# num= int(input("Enter a number : "))
# sum = 0
# while num > 0:
#     sum = sum + (num%10)
#     num= num//10

# print(f"the sum of digits is {sum}")


# =========================================================================================

# write a program to find least common multiple(LCM) of two numbers.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# for i in range (1,num2+1):
#     lcm = num1 * i
#     if lcm % num2 == 0:
#         print(f"the lcm is {lcm}")
#         break

# =========================================================================================

# write a program to find greatest common divisor(HCF or GCD) of two numbers.

# mera wala
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# def least(num1,num2):
#     if num1< num2 :
#         return num1
#     else:
#         return num2

# gcd = 1
# small = least(num1,num2)
# print(f"the small number is {small}")
# for i in range(2,small+1):
#     if num1 % i == 0 and num2 % i == 0:
#         gcd = i
# print(f"the gcd is {gcd}")


      
# # chatgpt wala 
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# def least(a, b):
#     return a if a < b else b

# small = least(num1, num2)
# print(f"The smaller number is {small}")

# gcd = 1
# for i in range(1, small + 1):
#     if num1 % i == 0 and num2 % i == 0:
#         gcd = i

# print(f"The GCD is {gcd}")

# =========================================================================================

# # LCM and HCF mix using ***euclidean theorem*** 
# def compute_hcf(a,b):
#     while b != 0:
#         a ,b = b, a%b
#     return a

# def compute_lcm (a,b):
#     hcf = compute_hcf(a,b)
#     lcm = (a * b) // hcf
#     return lcm 

# print(compute_hcf(5,12))
# print(compute_lcm(5,12))

# =================================================================================================

# # Create a program to check whether a number is prime or not 

# --------->> not an optimised way
# number =  int(input("Enter a number: "))
# for i in range(2,number):
#     if number % i == 0:
#         print("this is not a prime nummber")
#         break
#     else:
#         print("this is prime number")
#         break

# =========================================================================================

# # create a program to reverse the digits of a number

# number =  int(input("Enter a number: "))
# newNum = 0
# while number>0:
#     digit = number%10
#     newNum= newNum * 10 + digit
#     number = number // 10

# print(f"the reverser of number is {newNum}")

    
# =========================================================================================

# # create a program to find fibonacci series upto a entered number

# def fibonacci(number):
#     if number <= 0 :
#         return 
#     first = 0
#     print(first,end=" ")
#     second = 1
#     print(second,end=" ")
#     while number >= first + second :
#         third = first + second
#         print(third, end=" ") # this way it dont go to next line
#         first = second
#         second =  third

# number = int(input("Enter a number: "))
# print ("the fibonacci series is:")
# fibonacci(number)
    

# =========================================================================================

# # create a program to check if a number is armstrong number or not 

# def armstrongNum(num):
#     initNum = num
#     armNum = 0
#     digit_count = len(str(abs(num)))
#     while num>0:
#         digit = num % 10 
#         armNum = armNum + (digit ** digit_count)
#         num = num // 10
#     if initNum == armNum:
#         print("This is an Armstrong number.")
#     else:
#         print("This is not an Armstrong number.")

# number = int(input("Enter a number : "))
# armstrongNum(number)

# =========================================================================================

# # Create a program to check if a number is pallindrome or not ? 

# def pallindrome(num):
#     originalNum = num
#     initNum = 0
#     while num > 0:
#         digit = num % 10
#         initNum = initNum *10 + digit
#         num = num//10
#     if initNum == originalNum:
#         print("This is pallindrome")
#     else:
#         print("zthis is no pallindrome")

# number=int(input("Enter a number: "))
# pallindrome(number)





