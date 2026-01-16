# name="GibHon ADhiKArI"

# print(name.capitalize())

# student_profiles = {
#     "std_001": {
#         "name": "Alex",
#         "math_score": 85,
#         "science_score": 90,
#         "percentage": 87.5
#     },
#     "std_002": {
#         "name": "Jordan",
#         "math_score": 78,
#         "science_score": 82,
#         "percentage": 80.0
#     },
#     "std_003": {
#         "name": "Sam",
#         "math_score": 92,
#         "science_score": 88,
#         "percentage": 90.0
#     }
# }
# sorted_profiles = {k: v for k, v in sorted(student_profiles.items(), 
#                                           key=lambda x: x[1]["percentage"], 
#                                           reverse=True)}


# rank=0
# for std_id, profile in sorted_profiles.items():
#     print("----------------------------")
#     rank+=1
#     print(f'Rank :{rank}')
#     for key, value in profile.items():
#         if key=="name":
#             print(f"Name: {value}")
#         elif key=="math_score":
#             print(f"Math Score: {value}")
#         elif key=="science_score":
#             print(f"Science Score: {value}")
#         else:
#             print(f"Percentage: {value}%")    


# print(type("hello"))

# import random

# def gen_password(length=12):
#     chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789*!@#"
#     return "".join(random.choice(chars) for _ in range(length))

# def get_input(prompt, validate=lambda x: True, default=None):
#     while True:
#         value = input(prompt)
#         if not value and default is not None:
#             return default
#         if validate(value):
#             return value
#         print("Invalid input. Try again.")

# def sign_up(user_db, user_id, username, user_email, user_password, user_role, **extra_info):
#     user_db[user_id] = {
#         "username": username,
#         "user_email": user_email,
#         "user_password": user_password,
#         "user_role": user_role,
#         "user_gender": extra_info.get("user_gender", "Not recorded"),
#         "user_phone_no": extra_info.get("user_phone_number", "Not recorded"),
#         "user_address": extra_info.get("user_address", "Not recorded")
#     }
#     return user_id + 1

# # ==== MAIN ====
# user_db = {}
# user_id = 1

# print("Welcome to our Organization")
# entry_choice = input("Do you want to log-in or sign-up (log/sign): ").lower()

# if entry_choice == "sign":
#     username = get_input("Enter username (>=12 chars): ",
#                          validate=lambda x: len(x) >= 12).title()

#     user_email = get_input("Enter your e-mail: ",
#                            validate=lambda x: "@gmail.com" in x.lower())

#     user_password = get_input("Enter password or 'g' for random: ")
#     if user_password.lower() == "g":
#         length = get_input("Password length (12-25): ",
#                            validate=lambda x: x.isdigit() and 12 <= int(x) <= 25)
#         user_password = gen_password(int(length))

#     user_role = get_input("Enter role (staff/customer): ",
#                           validate=lambda x: x.lower() in ["staff", "customer"]).lower()

#     # Optional fields
#     user_gender = get_input("Enter gender (optional): ",
#                             validate=lambda x: x.isalpha() or x == "", default="Not recorded")
#     user_phone_number = get_input("Enter phone number (optional): ",
#                                   validate=lambda x: x.isdigit() or x == "", default="Not recorded")
#     user_address = get_input("Enter address (optional): ", default="Not recorded")

#     user_id = sign_up(user_db, user_id, username, user_email, user_password, user_role,
#                       user_gender=user_gender, user_phone_number=user_phone_number, user_address=user_address)

# print(user_db)


print("hello world")
