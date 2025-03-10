
# a single quote is use to asign a value
number_one = 1

# the double quote here is checking is the variable number_one is equal to the value of 2
if number_one == 2:
    # indentation is key when it comes to python so what 
    print(number_one)
else:
    print("false, the variable number_one is not greater than 2")


number_five = 5

# checking if the value of variable number_five is even or prime
# if the remainder of a number is zero after dividing it by 2 then its even if not it's prime
if number_five % 2 == 0:
    print(f"Yes!, number_five is a even number {number_five}")
else:
    print(f"No! is a prive number {number_five}")

my_name = "guyvenson"

# elif allows you to check more then one condition
if my_name == "john":
    print(f"my name is: {my_name} ")
elif my_name == "steven":
    print(f"hello {my_name}")
else:
    print(my_name)