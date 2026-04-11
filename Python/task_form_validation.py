import re

# Regular Expressions
patterns = {
    "username": r"^[A-Za-z0-9]{4,15}$",
    "mobile": r"^[6-9][0-9]{9}$",
    "gender": r"^(Male|Female|Other)$",
    "age": r"^(?:1[01][0-9]|120|[1-9]?[0-9])$",
    "dob": r"^\d{4}-\d{2}-\d{2}$",
    "email": r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",
    "password": r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_+]).{8,}$"
}

# Function to validate input
def validate_input(field_name, pattern):
    while True:
        value = input(f"Enter {field_name}: ")
        if re.fullmatch(pattern, value):
            return value
        else:
            print(f"❌ Invalid {field_name}, please try again.")

# Collecting user data
print("===== Form Validation =====")

username = validate_input("Username", patterns["username"])
mobile = validate_input("Mobile Number", patterns["mobile"])
gender = validate_input("Gender (Male/Female/Other)", patterns["gender"])
age = validate_input("Age", patterns["age"])
dob = validate_input("Date of Birth (YYYY-MM-DD)", patterns["dob"])
email = validate_input("Email ID", patterns["email"])
password = validate_input("Password", patterns["password"])

# Storing data in file
with open("data.txt", "a") as file:
    file.write(f"Username: {username}\n")
    file.write(f"Mobile: {mobile}\n")
    file.write(f"Gender: {gender}\n")
    file.write(f"Age: {age}\n")
    file.write(f"DOB: {dob}\n")
    file.write(f"Email: {email}\n")
    file.write(f"Password: {password}\n")
    file.write("-" * 30 + "\n")

print("✅ Data saved successfully in data.txt")

def delete_multiple_users(usernames_to_delete):
    try:
        with open("data.txt", "r") as file:
            records = file.read().split("-" * 30 + "\n")

        updated_records = []
        deleted_any = False

        for record in records:
            if record.strip() == "":
                continue

            # Check if any username matches
            if any(f"Username: {uname}" in record for uname in usernames_to_delete):
                deleted_any = True
                continue  # skip (delete)
            else:
                updated_records.append(record)

        if not deleted_any:
            print("❌ No matching users found.")
            return

        # Rewrite file
        with open("data.txt", "w") as file:
            for rec in updated_records:
                file.write(rec.strip() + "\n" + "-" * 30 + "\n")

        print("✅ Selected users deleted successfully.")

    except FileNotFoundError:
        print("❌ File not found.")

choice = input("Do you want to delete a user? (yes/no): ").lower()

if choice == "yes":
    username = input("Enter username to delete: ")
    delete_user(username)