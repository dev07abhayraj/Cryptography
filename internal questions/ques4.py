
# 4. Write a program to store the hash and salt using the PBKDF2_HMAC algorithm?

import hashlib
import os
import base64

def generate_salt(length=16):
    """Generate a random salt."""
    return os.urandom(length)

def hash_password(password, salt, iterations=100000, hash_name='sha256'):
    """Hash a password with the given salt using PBKDF2_HMAC."""
    password_bytes = password.encode('utf-8')  # Convert the password to bytes
    dk = hashlib.pbkdf2_hmac(hash_name, password_bytes, salt, iterations)
    return dk

def store_password(password, iterations=100000, hash_name='sha256'):
    """Generate salt and hash the password, then store them."""
    salt = generate_salt()
    hash_bytes = hash_password(password, salt, iterations, hash_name)
    
    # Encode salt and hash for storage (e.g., in a database)
    salt_b64 = base64.b64encode(salt).decode('utf-8')
    hash_b64 = base64.b64encode(hash_bytes).decode('utf-8')
    
    return salt_b64, hash_b64

def verify_password(stored_password, provided_password, stored_salt, iterations=100000, hash_name='sha256'):
    """Verify a provided password against the stored hash and salt."""
    salt = base64.b64decode(stored_salt.encode('utf-8'))
    stored_hash = base64.b64decode(stored_password.encode('utf-8'))
    
    provided_hash = hash_password(provided_password, salt, iterations, hash_name)
    
    return provided_hash == stored_hash

# Example usage:
password = "secure_password"

# Store the password
salt_b64, hash_b64 = store_password(password)
print("Salt (base64):", salt_b64)
print("Hash (base64):", hash_b64)

# Verify the password
is_valid = verify_password(hash_b64, password, salt_b64)
print("Password is valid:", is_valid)

# Verify with the wrong password
is_valid = verify_password(hash_b64, "wrong_password", salt_b64)
print("Password is valid:", is_valid)

