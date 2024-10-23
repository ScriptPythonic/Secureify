import re

class PasswordStrengthChecker:
    def __init__(self, password):
        self.password = password
        self.requirements_met = []

    def check_length(self):
        if len(self.password) >= 8:
            self.requirements_met.append("Length requirement met.")
        else:
            self.requirements_met.append("Length requirement not met. Consider using at least 8 characters.")

    def check_uppercase(self):
        if re.search(r'[A-Z]', self.password):
            self.requirements_met.append("Uppercase letter requirement met.")
        else:
            self.requirements_met.append("Uppercase letter requirement not met. Add at least one uppercase letter.")

    def check_lowercase(self):
        if re.search(r'[a-z]', self.password):
            self.requirements_met.append("Lowercase letter requirement met.")
        else:
            self.requirements_met.append("Lowercase letter requirement not met. Add at least one lowercase letter.")

    def check_numbers(self):
        if re.search(r'\d', self.password):
            self.requirements_met.append("Number requirement met.")
        else:
            self.requirements_met.append("Number requirement not met. Include at least one digit.")

    def check_special_characters(self):
        if re.search(r'[\W_]', self.password):
            self.requirements_met.append("Special character requirement met.")
        else:
            self.requirements_met.append("Special character requirement not met. Incorporate at least one special character.")

    def get_suggestions(self):
        suggestions = []
        if len(self.password) < 8:
            suggestions.append("Consider using at least 8 characters.")
        if not re.search(r'[A-Z]', self.password):
            suggestions.append("Add at least one uppercase letter.")
        if not re.search(r'[a-z]', self.password):
            suggestions.append("Add at least one lowercase letter.")
        if not re.search(r'\d', self.password):
            suggestions.append("Include at least one digit.")
        if not re.search(r'[\W_]', self.password):
            suggestions.append("Incorporate at least one special character.")
        return suggestions

    def assess_strength(self):
        """Assesses password strength based on met requirements."""
        self.check_length()
        self.check_uppercase()
        self.check_lowercase()
        self.check_numbers()
        self.check_special_characters()

        strength_score = len(self.requirements_met)
        strength = "Weak"
        
        if strength_score == 5:
            strength = "Strong"
        elif strength_score >= 3:
            strength = "Moderate"

        suggestions = self.get_suggestions()
        return strength, self.requirements_met, suggestions