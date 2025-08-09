import string

def check_password_strength(password):
    # Boolean variables to check presence of character types
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    # Integer variables for password length and character counts
    length = len(password)

    # Check password strength
    if length < 6:
        return "Weak", "Password is too short. It must be at least 6 characters long."
    elif has_upper and has_lower and has_digit and has_special:
        return "Strong", "Your password is strong!"
    elif (has_upper or has_lower) and has_digit:
        return "Medium", "Consider adding special characters to make your password stronger."
    else:
        return "Weak", "Your password is weak. Try including uppercase, lowercase, numbers, and special characters."

def main():
    password_history = []  # List to store previously entered passwords

    while True:
        password = input("Enter a password: ")
        password_history.append(password)

        strength, feedback = check_password_strength(password)
        print(feedback)

        if strength == "Strong":
            print("Congratulations! You have set a strong password.")
            break
        elif strength == "Medium":
            print("Tip: Add special characters to make your password stronger.")
        elif strength == "Weak":
            print("Tip: Try including a mix of uppercase, lowercase, numbers, and special characters.")

    print("Password History:", password_history)

if __name__ == "__main__":
    main()
