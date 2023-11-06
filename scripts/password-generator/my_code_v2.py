# Generate password of a given length
# run as: python my_code_v2.py
# you will be asked to type the length of the password

import secrets, string

# define alphabet
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

# define function
def generate_password():
    """Generate a random password of a given length
    """
    password = ''
    length = int(input("\nType the length of the password you want to generate: "))

    for i in range(length):
        if i==0:
            password += ''.join(secrets.choice(string.ascii_uppercase))
        else:
            password += ''.join(secrets.choice(alphabet))
    
    print(f"\nYour new password is: \n", password, "\n")

# call the function
generate_password()