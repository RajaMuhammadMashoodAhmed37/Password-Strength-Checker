

import re


def check_password_strength(password):
    # Check length
    if len(password) < 8:
        return "Password is too short. It must be at least 8 characters long."

    # Check for uppercase letter
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."

    # Check for lowercase letter
    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter."

    # Check for digit
    if not re.search(r"\d", password):
        return "Password must contain at least one digit."

    # Check for special character
    if not re.search(r"[!@#$%^&*()-+]", password):
        return "Password must contain at least one special character."

    return "Password is strong."            

def main():
    password = input("Enter a password to check its strength: ")
    result = check_password_strength(password)
    print(result)

if __name__ == "__main__":
    main()