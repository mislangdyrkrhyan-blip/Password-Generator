import secrets
import string


def generate_password(length=8):
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    special = "!@#$%^&*"

    # Guarantee one character from each required category
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(numbers),
        secrets.choice(special)
    ]

    # Fill the remaining characters
    all_characters = lowercase + uppercase + numbers + special

    for _ in range(length - 4):
        password.append(secrets.choice(all_characters))

    # Securely shuffle the password
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


# Generate a password
password = generate_password()
print(password)
