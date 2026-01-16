import random

#---------------------------------------------------------------------------------------------Functions----------------------------------------------------------------------------------------------------------- 
# Random Password Generator
def gen_password(length = 12):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789*!@#"
    return "".join(random.choice(chars) for _ in range(length))

# Sign up Function
def sign_up(user_database, user_id, username, user_email, user_password, user_role, **extra_info):
    user_database[user_id]={
        "username": username,
        "user_email":user_email,
        "user_password":user_password,
        "user_role":user_role,
        "user_gender":extra_info.get("user_gender","Not recorded") ,
        "user_phone_no":extra_info.get("user_phone_number","Not recorded"),
        "user_address":extra_info.get("user_address","Not recorded")
    }
    user_id += 1
    return user_id


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# The Global Variables and Database dictionary
user_database = {}
user_id = 1
staff_code = gen_password(6)

# Printing the system
print("Welcome to our Organization")

entry_choice = (input("Do you want to log-in or sign-up(log to log-in /sign to sign-up):")).lower()
# -----------------------------------------------------------------------------------------------Sign-in-----------------------------------------------------------------------------------------------------------

if entry_choice == "sign":
    username_data_status = False
    username = input("Enter an username(atleast 12 characters):")
    while username_data_status == False:
        if len(username) < 12:
            print("Invalid Username.Please enter a username again!")
            username = input("Enter the username:")
        else:
            username_data_status = True  
    username = username.strip()
            
    user_email = input("Enter your e-mail:")
    email_data_status = False
    while email_data_status == False:
        if user_email.find("@gmail.com") == -1 :
            print("Invalid e-mail.Please enter a e-mail again!")
            user_email = input("Enter the e-mail:")
        else:
            email_data_status = True
    
    user_password = input("Enter your password or Enter 'g' to create a random password:")
    if user_password == "g":
        length_password = input("Enter the length for your password(12-25):")
        while not length_password.isdigit():
            print("Invalid length.Please input password length again")
            length_password = (input("Enter the length of your password"))
        length_password = int(length_password)
        while length_password > 25 or length_password < 12:
            print("Please choose a length between 12 to 25.")
            length_password = input("Enter the length of your password")
            length_password = int(length_password)
        user_password = gen_password(length_password)
            
    user_role = (input("Enter your role(admin/staff/customer):")).lower()
    role_data_status = False
    while role_data_status == False:
        if user_role not in ["staff", "customer"]:
            print("Invalid role.Please enter a role again!")
            user_role=input("Enter the role:").lower()
        else:
            role_data_status = True
    if user_role == "staff":
    trials = 0
    while trials < 3:
        code_input = input(f"Enter secret code: ")
        if code_input == staff_code:
            user_role = "staff"
            trials = 3 
        else:
            trials += 1
            user_role = "customer" # Defaulting them as they fail
            print(f"Incorrect. {3 - trials} chances left.")
    if user_role == "customer":
        print("You are an imposter and your role has been defaulted to customer.")
        
    user_gender = input("Enter your gender(optional):").lower()
    gender_data_status = False
    while gender_data_status == False:
        if not user_gender.isalpha():
            print("Invalid gender.Please enter a gender again!").lower()
            user_gender = input("Enter the gender:")
        else:
            gender_data_status = True

    user_phone_number = input("Enter your phone number(optional):")
    phoneNO_data_status = False
    while phoneNO_data_status == False:
        if not user_phone_number.isdigit():
            print("Invalid phone number.Please enter a phone number again!")
            user_phone_number=input("Enter the phone number:")
        else:
            phoneNO_data_status = True
    
    user_address = input("Enter your temoparary address(optional):")
    
    user_id=sign_up(user_database, user_id, username, user_email, user_password, user_role,user_gender=user_gender, user_phone_number=user_phone_number, user_address=user_address) 
# ------------------------------------------------------------------------------------------------Log-In----------------------------------------------------------------------------------------------------------