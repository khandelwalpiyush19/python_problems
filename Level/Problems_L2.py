# Pattern printing 
#     *                * * * *                *
#     * *              * * *                * *
#     * * *            * *                * * *
#     * * * *          *                * * * *


# # first pattern
# number = int(input("Enter a number: "))
# for i in range(1,number+1):
#     for j in range(1,i+1):
#         print("* " ,end=" ")
#     print()


# ====================================================================================

# # second pattern 

# number = int(input("Enter a number: "))
# for i in range(number,0,-1):
#     for j in range(1,i+1):
#         print("* " ,end=" ")
#     print()

# ====================================================================================

# # third pattern
# number = int(input("Enter a number: "))
# for i in range(1,number+1):
#     # pehle space k liye fir star k liye loop chalao
#     for j in range(number-i):
#         print(" " , end ="")
#     for stars in range (i):
#         print("*" , end ="")
#     print()

# =============================================================================

#  # fourth pattern(pyramid) 
# number = int(input("Enter a number: "))
# for i in range(1,number+1):
#     # pehle space k liye fir star k liye loop chalao
#     for j in range(number-i):
#         print(" " , end ="")
#     for stars in range (i):
#         print("* " , end ="") # space nly give and make a pattern 
#     print()
        