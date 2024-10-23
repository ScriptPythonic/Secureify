import hashlib
import requests

class PasswordBreachChecker:
    API_URL = "https://api.pwnedpasswords.com/range/"

    @staticmethod
    def hash_password(password):
        """Hashes the given password using SHA-1."""
        sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        return sha1_hash

    @classmethod
    def check_breach(cls, password):
        """Checks if the given password has been exposed in a data breach."""
        sha1_hash = cls.hash_password(password)
        # Use the first 5 characters of the hash for the API request
        prefix = sha1_hash[:5]
        response = requests.get(f"{cls.API_URL}{prefix}")

        if response.status_code != 200:
            raise Exception("Error querying the API")

        # Check if the hash is in the response
        hash_suffix = sha1_hash[5:]
        for line in response.text.splitlines():
            hash, count = line.split(':')
            if hash == hash_suffix:
                return f"This password has been exposed {count} times in data breaches."
        
        return "This password has not been found in any data breaches."
