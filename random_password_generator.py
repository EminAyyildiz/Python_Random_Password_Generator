
#Written by Emin Ayyıldız
print("Written by Emin Ayyıldız")

import random
import string

def random_password_generator(length_of_pass):
    password = ""
    if choice == 1:
        for i in range(length_of_pass):
            password = password + random.choice(string.ascii_letters)
        return password
    elif choice == 2:
        for i in range(length_of_pass):
            password = password + random.choice(string.digits + string.ascii_letters)
        return password
    else:
        return password

while True:
  length_of_pass = int(input("Enter the number of digits you want to create a password: "))
  choice = int(input("1- I want only letters in the password.\n2- I want the password to be mixed letters and numbers.\n3- EXIT \n----> "))

  print(random_password_generator(length_of_pass))
  if choice == 3:
    print("We hope your password is secure enough. :)) BYE BYE...")
    break
