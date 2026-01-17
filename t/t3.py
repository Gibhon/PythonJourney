import random
import json

#---------------------------------------------------------------------------------Functions---------------------------------------------------------------------- 
# Random Password Generator
def gen_password(length=12):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789*!@#"
    return "".join(random.choice(chars) for _ in range(length))

# Sign up Function
def sign_up(user_database, user_id, username, user_email, user_password, user_role, **extra_info):
    user_database[str(user_id)] = {
        "username": username,
        "user_email": user_email,
        "user_password": user_password,
        "user_role": user_role,
        "user_gender": extra_info.get("user_gender", "Not recorded"),
        "user_phone_no": extra_info.get("user_phone_number", "Not recorded"),
        "user_address": extra_info.get("user_address", "Not recorded")
    }
    with open("t3db.json", "w") as file:
        json.dump(user_database, file, indent=4) 
    print(f"Registration successful! Your User ID is: {user_id}")
    return user_id + 1

# Username Validator
def username_validator(username):
    while len(username.strip()) < 12:
        print("Invalid Username. Must be at least 12 characters.")
        username = input("Enter the username: ")
    return username.strip()

# E-mail Validator
def email_validator(user_email):
    while "@gmail.com" not in user_email:
        print("Invalid e-mail. Please use a @gmail.com address.")
        user_email = input("Enter the e-mail: ")
    return user_email

# Password generator
def password_generator(user_password):
    if user_password.lower() == "g":
        while True:
            length_input = input("Enter password length (12-25): ")
            if length_input.isdigit() and 12 <= int(length_input) <= 25:
                length_password = int(length_input)
                generated = gen_password(length_password)
                print(f"Your generated password is: {generated}")
                
                choice = input("Press 'r' to re-generate or any other key to accept: ").lower()
                if choice != 'r':
                    return generated
            else:
                print("Invalid length. Please choose between 12 and 25.")
    return user_password

# Role Validator
def role_validator(user_role, staff_code, admin_code):
    while user_role not in ["staff", "customer", "admin"]:
        print("Invalid role. Please choose 'staff' or 'customer' or 'admin'.")
        user_role = input("Enter the role: ").lower()
    
    if user_role == "staff":
        trials = 0
        while trials < 3:
            code_input = input("Enter secret code: ")
            if code_input == staff_code:
                print("Access Granted: Staff Role Assigned.")
                return "staff"
            else:
                trials += 1
                print(f"Incorrect. {3 - trials} chances left.")
        
        print("Verification failed. Role defaulted to customer.")
        return "customer"
    if user_role == "admin":
        trials = 0
        while trials < 3:
            code_input = input("Enter secret code: ")
            if code_input == admin_code:
                print("Access Granted: Admin Role Assigned.")
                return "admin"
            else:
                trials += 1
                print(f"Incorrect. {3 - trials} chances left.")
        
        print("Verification failed. Role defaulted to customer.")
        return "customer"
    
    return user_role

# Alpha Validator
def isalpha_validator(value, value_string):
    if value == "": return "Not recorded"
    while not value.isalpha():
        print("Invalid input! Only letters allowed.")
        value = input(f"Enter {value_string} again: ")
        if value == "": return "Not recorded"
    return value

# Isdigit Validator
def isdigit_validator(value, value_string):
    if value == "": return "Not recorded"
    while not value.isdigit():
        print("Invalid input! Only numbers allowed.")
        value = input(f"Enter {value_string} again: ")
        if value == "": return "Not recorded"
    return value

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Main Logic

try:
    with open("t3db.json", "r") as file:
        user_database = json.load(file)
    # Get the highest ID and add 1
    if user_database:
        user_id = max(int(k) for k in user_database.keys()) + 1
    else:
        user_id = 1
except (FileNotFoundError, json.JSONDecodeError):
    user_database = {
        "0": {
            "username": "Gibhon Adhikari",
            "user_email": "admin@gmail.com",
            "user_password": "AdminPassword123",
            "user_role": "admin",
            "user_gender": "male",
            "user_phone_no": "980",
            "user_address": "Pokhara,Nepal"
        }
    }
    user_id = 1

staff_code = "TheSecretSauce"
admin_code = "AuthorityKey"

print("--- Welcome to our Organization ---")
entry_choice = input("Do you want to log-in or sign-up (log/sign): ").lower()

# -----------------------------------------------------------------------------------------------Sign-up--------------------------------------------------------------------
if entry_choice == "sign":
    username = username_validator(input("Enter a username (at least 12 characters): "))
    user_email = email_validator(input("Enter your e-mail: "))
    
    user_password = input("Enter password or 'g' to generate: ")
    user_password = password_generator(user_password)

    user_role = role_validator(input("Enter role (staff/customer): ").lower(), staff_code, admin_code)
  
    user_gender = isalpha_validator(input("Enter gender (optional, press enter to skip): "), "gender")
    user_phone_number = isdigit_validator(input("Enter phone number (optional, press enter to skip): "), "phone number")
    user_address = input("Enter temporary address (optional): ")
    if not user_address: user_address = "Not recorded"
    
    user_id = sign_up(user_database, user_id, username, user_email, user_password, user_role, 
                      user_gender=user_gender, user_phone_number=user_phone_number, user_address=user_address)

# ------------------------------------------------------------------------------------------------Log-In--------------------------------------------------------------------
elif entry_choice == "log":
    uid_input = input("Enter your user_id: ")
    password_input = input("Enter your password: ")
    
    if uid_input in user_database:
        trials = 0
        while trials < 3:
            if user_database[uid_input]["user_password"] == password_input:
                print(f"Welcome back, {user_database[uid_input]['username']}! You are logged in.")
            else:
                trials += 1
                print(f"Incorrect. {3 - trials} chances left.") 
        if trials == 3:
            print("You won't get access to this organization")
        else:
            print("Incorrect password.")
    else:
        print("User ID not found.")
else:
    print("Invalid option selected.")