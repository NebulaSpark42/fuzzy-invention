import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    """Generate a strong random password with given preferences."""
    
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits if use_digits else ""
    special_chars = string.punctuation if use_special_chars else ""
    
    all_chars = letters + digits + special_chars

    if len(all_chars) == 0:
        return "Error: No character set selected!"
    
    # Generate a random password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

if __name__ == "__main__":
    # Ask user for preferences
    length = int(input("Enter password length: "))
    use_digits = input("Include digits? (y/n): ").strip().lower() == "y"
    use_special_chars = input("Include special characters? (y/n): ").strip().lower() == "y"

    # Generate and print password
    new_password = generate_password(length, use_digits, use_special_chars)
    print(f"Generated Password: {new_password}")
