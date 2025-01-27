#Text Based Calculator

#the try and except function makes sure the user enters a number
#try:
#    number1 = float(number1)
#    number2 = float(number2)
#except:
#   print("Invalid, Not a number!")

#We are creating a function called get_number to get 2 numbers from the user
#def get_number(number) -> number here is a parameter so we can add Number 1 and Number 2 later on
#float() converts the strings inputted by the user from strings to numbers

def get_number(number):
    while True:
        number1 = input("Number " + str(number)+ ": ")
        try:
            return float(number1)
        except:
            print("Invalid, Not a number!")

number1 = get_number(1)
number2 = get_number(2)
sign = input("Input a sign (+ - * /): ")

#Result = 0 here so we can define it and have no errors later on
result = 0

if sign == "+":
    result = number1 + number2
elif sign == "-":
    result = number1 - number2
elif sign == "/":
    if number2 == "0": 
        print("You can't divide a number by 0")
    else:
        result = number1 / number2
elif sign == "*":
    result = number1 * number2

print(result)