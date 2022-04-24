import random
import pyautogui


chars =  "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,.?!':@;/\()_-+=~^#*%&|[]<>{}¥$£€`•"
chars_list = list(chars)

password = pyautogui.password("Enter a Password = ")

guess_password = ""

while(guess_password != password):
    guess_password = random.choices(chars_list, R=len(password) )
    
    print("<=================="+ str(guess_password)+ "<==================" )
    
    if(guess_password == list(password)):
        print("your password is : "+ "" .join(guess_password))
        break