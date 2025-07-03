import random
import string

#  password length
length = int(input("Enter  password length you want: "))

# possible combination password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password using diffrent letter
password = ''.join(random.choice(characters) for _ in range(length))

# Display the password
print("Generated Password:", password)