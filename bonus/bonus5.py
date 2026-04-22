# Create a program that checkes for Password Strenght
# Must be 8 characters long, atleast one number, one Uppercase letter


password = input("Enter a password: ")

result = []

#Condition if password is 8 characters or longer:
if len(password) >= 8:
    result.append(True)

else:
    result.append(False)

#Condition Check digits
digit = False
for i in password:
    if i.isdigit():
        digit = True

result.append(digit)


#Condition if password has Uppercase letter
capital = False
for i in password:
    if i.isupper():
        capital = True

result.append(capital)


# Check reach value of the result list, if all is true then good, if false then bad
if all(result):
    print("Strong password")

else:
    print("Weak password")

