# print("Welcome to the rollercoster")
# height = int(input("What is your height in cm?\n"))

# if height > 120:
#     print("You can ride the rollercoaster")
#     age = int(input("what's your age?\n"))
#     if age < 12:
#         print("Please pay $5")
#     elif age <= 18:
#         print("Please pay $7")
#     else:
#         print("Please pay $12")
# else:
#     print("Sorry, you have to grow taller before you can ride")


# num = int(input("Input any number you like\n"))

# if num % 2 == 0:
#     print("That's an even number")
# else:
#     print("That's an odd number")


# print("Welcome to the BMI calculator\n")
# weight = input("Please inpt your weight?\n")
# height = input("What's your height?\n")
# bmi_index = int(float(weight) / float(height)**2)

# if bmi_index < 18.5:
#     print("Your BMI index is " + str(bmi_index) +
#           " which means you're UNDERWEIGHT")
# elif bmi_index < 25:
#     print("Your BMI index is " + str(bmi_index) +
#           " which means you have a NORMAL WEIGHT")
# elif bmi_index < 30:
#     print(f"Your BMI index is {bmi_index} which means you're OVERWEIGHT")
# elif bmi_index < 35:
#     print(f"Your BMI index is {bmi_index} which means you're OBESE")
# else:
#     print(f"You're clinically obese")


# print("Welcome to the leap year calculator")

# year = int(input("Please type in any year to check whether it's a leap year\n"))

# if year %4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("That's a leap year")
#         else:
#             print("That's not a leap year")
#     else:
#         print("That's a leap year")
# else:
#     print("that's not a leap year")


pizza_order = input(
    "Please input your pizza order. Type s for small, m for medium and l for large pizza\n")
extra_pep = input("Do you want pepperoni? Type y or n\n")
total_bill = 0

extra_cheese = input("Do you need extra cheese? Type y or n\n")

if extra_cheese == "y":
    total_bill += 1
else:
    total_bill += 0


if pizza_order == "s":
    total_bill += 15
    if extra_pep == "y":
        print(f"Your total bill is ${total_bill + 2} dollars")
    else:
        print(f"Your total bill is {total_bill} dollars")
elif pizza_order == "m":
    total_bill += 20
    if extra_pep == "y":
        print(f"Your total bill is ${total_bill + 3} dollars")
    else:
        print(f"Your total bill is {total_bill} dollars")
elif pizza_order == "l":
    total_bill += 25
    if extra_pep == "y":
        print(f"Your total bill is ${total_bill + 3} dollars")
    else:
        print(f"Your total bill is {total_bill} dollars")
else:
    print("You need to make an order please")
