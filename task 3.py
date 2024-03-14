import re


def assess_password_strength(password):
    # Define regex patterns for different criteria
    patterns = {
        'length': r'.{8,}',
        'uppercase': r'[A-Z]',
        'lowercase': r'[a-z]',
        'number': r'\d',
        'special_char': r'[!@#$%^&*(),.?":{}|<>]'
    }

    # Initialize strength score
    strength_score = 0
    criteria_met = []

    # Assess each criteria
    for key, pattern in patterns.items():
        if re.search(pattern, password):
            strength_score += 1
            criteria_met.append(key)

    # Assess length separately
    if strength_score >= 4 and len(password) >= 12:
        strength_score += 1
        criteria_met.append('length')

    # Return the strength score and criteria met
    return strength_score, criteria_met

def main():
    while True:
        password = input("Enter your password (type 'exit' to quit): ")

        if password.lower() == 'exit':
            print("Exiting the program...")
            break

        strength_score, criteria_met = assess_password_strength(password)

        # Print strength assessment and feedback
        print("\nPassword strength assessment:")
        print(f"Strength score: {strength_score}/6")
        print("Criteria met:")
        for criteria in criteria_met:
            print(f"- {criteria}")

        # Give specific feedback based on strength score
        if strength_score == 6:
            print("Feedback: Password is very strong")
        elif strength_score >= 4:
            print("Feedback: Password is strong")
        elif strength_score >= 2:
            print("Feedback: Password is moderate")
        else:
            print("Feedback: Password is weak")

if __name__ == "__main__":
    main()
