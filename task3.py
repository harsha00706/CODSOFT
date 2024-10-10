import random
password = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&"
maxLength = int(input("Enter the length of the password : "))
generatedPassword = "".join(random.sample(password,maxLength))
print(f"Your generated password is : {generatedPassword}")