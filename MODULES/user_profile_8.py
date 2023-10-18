"""
8
Enhancing User Profiles:
Define a dictionary that represents a user's profile with keys for name, age,
 email, and city. Create a Python module named user_profile.py that contains a 
function to import the user's profile. In a separate script, import the
 user_profile module, ask the user for additional information like a phone
 number, and update the dictionary with the new data. Finally, print the updated
 profile.
"""

def import_user_profile():
    user_profile = {
        "name": "John Doe",
        "age": 30,
        "email": "johndoe@example.com",
        "city": "Anytown"
    }
    return user_profile