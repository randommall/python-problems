from user_profile_8 import import_user_profile

user_profile = import_user_profile()

phone_number = input("Enter your phone number: ")

user_profile["phone_number"] = phone_number

print("Updated User Profile:")

for key, value in user_profile.items():
    print(f"{key}: {value}")