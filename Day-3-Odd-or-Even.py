# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
E_or_O_number = number % 2

if E_or_O_number == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")