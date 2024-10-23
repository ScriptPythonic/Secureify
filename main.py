from Secureify import PasswordBreachChecker, PasswordStrengthChecker

def main():
    password = input("Enter your password to check for breaches: ")
    
    # Check for breaches
    breach_checker = PasswordBreachChecker()
    breach_result = breach_checker.check_breach(password)
    print(breach_result)
    
    # Check password strength
    strength_checker = PasswordStrengthChecker()
    strength_result = strength_checker.check_strength(password)
    print(strength_result)

if __name__ == "__main__":
    main()
