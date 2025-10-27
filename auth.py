import hashlib
import os

class AuthSystem:
    def __init__(self, users_file='users.txt'):
        self.users_file = users_file
        if not os.path.exists(self.users_file):
            with open(self.users_file, 'w') as f:
                f.write('')
    
    def hash_password(self, password):
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register(self, username, password, email):
        """Register a new user"""
        # Check if username already exists
        with open(self.users_file, 'r') as f:
            for line in f:
                if line.strip():
                    stored_username = line.split(',')[0]
                    if stored_username == username:
                        return False, "Username already exists"
        
        # Add new user
        hashed_pw = self.hash_password(password)
        with open(self.users_file, 'a') as f:
            f.write(f"{username},{hashed_pw},{email}\n")
        return True, "Registration successful"
    
    def login(self, username, password):
        """Login user"""
        hashed_pw = self.hash_password(password)
        with open(self.users_file, 'r') as f:
            for line in f:
                if line.strip():
                    stored_username, stored_password, _ = line.strip().split(',')
                    if stored_username == username and stored_password == hashed_pw:
                        return True, "Login successful"
        return False, "Invalid username or password"
    
    def forgot_password(self, username, email, new_password):
        """Reset password if username and email match"""
        lines = []
        found = False
        
        with open(self.users_file, 'r') as f:
            for line in f:
                if line.strip():
                    stored_username, stored_password, stored_email = line.strip().split(',')
                    if stored_username == username and stored_email == email:
                        hashed_pw = self.hash_password(new_password)
                        lines.append(f"{username},{hashed_pw},{email}\n")
                        found = True
                    else:
                        lines.append(line)
        
        if found:
            with open(self.users_file, 'w') as f:
                f.writelines(lines)
            return True, "Password reset successful"
        return False, "Username and email do not match"