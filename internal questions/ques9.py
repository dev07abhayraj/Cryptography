#  write a program for Add a User & password with pbkdf2_hmac?

import hashlib
import os
import base64
import json

def generate_salt(length=16):
    """Generate a random salt."""
    return os.urandom(length)

def hash_password(password, salt, iterations=100000, hash_name='sha256'):
    """Hash a password with the given salt using PBKDF2_HMAC."""
    password_bytes = password.encode('utf-8')  # Convert the password to bytes
    dk = hashlib.pbkdf2_hmac(hash_name, password_bytes, salt, iterations)
    return dk

def add_user(username, password, user_db, iterations=100000, hash_name='sha256'):
    """Add a new user with a hashed password to the user database."""
    salt = generate_salt()
    hash_bytes = hash_password(password, salt, iterations, hash_name)
    
    # Encode salt and hash for storage
    salt_b64 = base64.b64encode(salt).decode('utf-8')
    hash_b64 = base64.b64encode(hash_bytes).decode('utf-8')
    
    # Store the username, salt, and hash in the database
    user_db[username] = {
        'salt': salt_b64,
        'hash': hash_b64,
        'iterations': iterations,
        'hash_name': hash_name
    }

def save_user_db(user_db, filename='user_db.json'):
    """Save the user database to a file."""
    with open(filename, 'w') as f:
        json.dump(user_db, f)

def load_user_db(filename='user_db.json'):
    """Load the user database from a file."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def main():
    user_db = load_user_db()

    print("Add a new user")
    username = input("Enter username: ")
    password = input("Enter password: ")

    add_user(username, password, user_db)
    save_user_db(user_db)

    print(f"User '{username}' added successfully!")

if __name__ == "__main__":
    main()
