import bcrypt


def hash_password(password, cost_factor=12):
    """Hashes a password with a random salt.

    Args:
        password (str): The password to hash.
        cost_factor (int, optional): The cost factor for hashing. Defaults to 12.

    Returns:
        str: The hashed password.
    """
    salt = bcrypt.gensalt(cost_factor)
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    return hashed_password


def verify_password(password, hashed_password):
    """Verifies if a password matches a hashed password.

    Args:
        password (str): The password to verify.
        hashed_password (str): The hashed password to compare against.

    Returns:
        bool: True if the password matches the hashed password, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
