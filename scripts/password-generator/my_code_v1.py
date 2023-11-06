# Generate password of a given length
# run as: python my_code_v1.py -l 10

import secrets, string
import argparse

# parsers
parser = argparse.ArgumentParser(description='Password generator')
parser.add_argument('-l', '--length', type=int, required=True, help='password length')
args = parser.parse_args()

# define alphabet
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

# define function
def generate_password(length=8):
    """Generate a random password of a given length
    """
    password = ''
    for i in range(length):
        if i==0:
            password += ''.join(secrets.choice(string.ascii_uppercase))
        else:
            password += ''.join(secrets.choice(alphabet))
    
    print("Your new password is: \n", password)

# call the function
generate_password(length=args.length)