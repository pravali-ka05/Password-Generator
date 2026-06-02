import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password

print("===== PASSWORD GENERATOR =====")

count = int(input("How many passwords do you want? "))
length = int(input("Enter password length: "))

for i in range(count):
    password = generate_password(length)
    print(f"Password {i+1}: {password}")