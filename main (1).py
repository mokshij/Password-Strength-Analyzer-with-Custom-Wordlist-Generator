import re
import string
import random

def assess_password_strength(password):
    # Checking criteria
    has_numbers = any(char.isdigit() for char in password)
    has_upper_case = any(char.isupper() for char in password)
    has_lower_case = any(char.islower() for char in password)
    meets_length_requirement = len(password) >= 12  # Minimum length of 12 characters
    has_special_characters = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    # Count the number of criteria met
    criteria_met = sum([has_numbers, has_upper_case, has_lower_case, meets_length_requirement, has_special_characters])

    # Provide feedback on unmet criteria
    feedback = []
    if not has_numbers:
        feedback.append("Include at least one number.")
    if not has_upper_case:
        feedback.append("Include at least one uppercase letter.")
    if not has_lower_case:
        feedback.append("Include at least one lowercase letter.")
    if not meets_length_requirement:
        feedback.append("Make sure your password is at least 12 characters long.")
    if not has_special_characters:
        feedback.append("Include at least one special character.")

    # Determine password strength based on criteria met
    if criteria_met == 5:
        return "Password Strength Level: Very Strong (All criteria are met).", []
    elif criteria_met == 4:
        return "Password Strength Level: Strong (4 out of 5 criteria are met).", feedback
    elif criteria_met == 3:
        return "Password Strength Level: Moderate (3 out of 5 criteria are met).", feedback
    else:
        return "Password Strength Level: Weak (Less than 3 criteria are met).", feedback

def generate_strong_password(length=12):
    if length < 12:
        print("Please choose a password length of at least 12 characters.")
        return None

    # Create a pool of characters for the password
    all_characters = (
        string.ascii_letters + 
        string.digits + 
        string.punctuation
    )
    
    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("---------------- Password Complexity Checking Tool -----------------")
    print("Here are some quick tips for creating a secure password:")
    tips = [
        "1. Length: Aim for at least 12 characters.",
        "2. Mix Characters: Use a combination of uppercase, lowercase, numbers, and symbols.",
        "3. Avoid Common Words: Don't use easily guessable information.",
        "4. No Personal Info: Avoid using names, birthdays, or personal details.",
        "5. Use Passphrases: Consider combining multiple words or a sentence.",
        "6. Unique for Each Account: Don't reuse passwords across multiple accounts.",
        "7. Regular Updates: Change passwords periodically.",
        "8. Enable 2FA: Use Two-Factor Authentication where possible.",
        "9. Be Wary of Phishing: Avoid entering passwords on suspicious sites.",
        "10. Password Manager: Consider using one for secure and unique passwords."
    ]
    for tip in tips:
        print(tip)

    while True:
        action = input("\nWould you like to (c)heck a password or (g)enerate a strong password? (q to quit): ").strip().lower()
        
        if action == 'c':
            password_input = input("Enter your password: ")
            if not password_input:
                print("Password cannot be empty. Please try again.")
                continue
            
            # Assess the password strength
            result, feedback = assess_password_strength(password_input)

            # Display the masked password and strength result
            masked_password = password_input[0] + '#' * (len(password_input) - 2) + password_input[-1] if len(password_input) > 2 else password_input
            print("\nEntered Password: {}".format(masked_password))
            print(result)
            
            # Display feedback if there are suggestions
            if feedback:
                print("Suggestions to improve your password:")
                for suggestion in feedback:
                    print(f"- {suggestion}")

        elif action == 'g':
            length = int(input("Enter the desired length for the password (minimum 12): "))
            password = generate_strong_password(length)
            if password:
                print(f"Here’s your strong password: {password}")

        elif action == 'q':
            print("Thanks for using the password checker. Goodbye!")
            break

        else:
            print("Hmm, that didn't seem to be a valid option. Please enter 'c', 'g', or 'q'.")

if __name__ == "__main__":
    main()
