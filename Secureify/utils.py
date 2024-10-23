import re

def provide_strength_feedback(password):
    """Provide feedback on password strength."""
    feedback = []

    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters.")
    if not re.search(r"[A-Z]", password):
        feedback.append("Password should include at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        feedback.append("Password should include at least one lowercase letter.")
    if not re.search(r"[0-9]", password):
        feedback.append("Password should include at least one digit.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        feedback.append("Password should include at least one special character.")
    
    if not feedback:
        return "Your password is strong."
    
    return " ".join(feedback)
