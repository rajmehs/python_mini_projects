import random
import string

def generate_password(length=12):
    """
    Generate a random secure password.
    Default length is 12 characters.
    """

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    print("🔐 Welcome to Password Generator")
    length = int(input("Enter password length: "))
    print("Your generated password is:")
    print(generate_password(length))
