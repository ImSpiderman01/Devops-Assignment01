import re

def check_password_strength(password):
    # Minimum length check
    if len(password) < 8:
        return False

    # Check for uppercase, lowercase, digit, special character
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False

    return True


# Script section
if __name__ == "__main__":
    password = input("Enter a password to check strength: ")

    if check_password_strength(password):
        print("Strong password ✔️")
    else:
        print("Weak password ❌  — must include:")
        print("- Minimum 8 characters")
        print("- Uppercase & lowercase letters")
        print("- At least one digit")
        print("- At least one special character (!@#$ etc.)")
