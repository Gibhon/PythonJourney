print("Welcome to Sentry Validator")


full_name=input("Enter your full name:")

name_components=full_name.split()
# for i in range(len(name_components)):
#     name_components[i]=name_components[i].capitalize()
name_components=[comp.capitalize() for comp in name_components]
full_name=" ".join(name_components)

username=input("Enter a username:")

while len(username)<12 or not  username.find(" ")==-1:
    print("Invalid Username")
    username=input("Enter the username again:")


scholarship_goals=float(input("Enter your scholarship goals:"))
security_deposit=round(scholarship_goals*0.1, 2)


print(f"server1 sentry_validator[1001]: INFO - Welcome {full_name} to the best sentry validator made by me.")
print(f"server1 sentry_validator[1001]: INFO -Your username is set as{username}.")
print(f"server1 sentry_validator[1001]: INFO -Your scholarship goals have been set to {scholarship_goals} .")
if scholarship_goals<1000000:
    print(f"server1 sentry_validator[1001]: WARNING-{scholarship_goals} amount as goal might not be enough.")
print(f"server1 sentry_validator[1001]: INFO -Your security deposit is {security_deposit} .")
