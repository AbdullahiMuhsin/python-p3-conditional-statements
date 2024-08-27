#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    lowercase_username = username.lower()
    if lowercase_username == "admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
    
result = admin_login("ADMIN", "12345")
print(result) 


def hows_the_weather(temperature):
    # your code here
    if temperature < 40:     
        return "It's brisk out there!"
    elif temperature >= 40 and temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else: 
        return "It's perfect out there!"

result = hows_the_weather(77)
print(result)
    

result = hows_the_weather(33)
print(result)


def fizzbuzz(num):
    # your code here
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

result = fizzbuzz(15)
print(result)


def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")

result = calculator("+", 1, 2)
print(result)

try:
    result = calculator("a", 1, 2)
except:
    print("Invalid operation!")

result = calculator("+", 1, 2)
print(result)


