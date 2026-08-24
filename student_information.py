full_name = input("Enter your full name: ")
student_id = input("Enter your student ID: ")
programme = input("Enter your programme: ")
level = input("Enter your level: ")
age = input("Enter your age: ")
favourite_language = input("Enter your favourite programming language: ")


# Generate student username and email using string concatenation
username = full_name[:3].lower() + student_id
email = username + "@st.ug.edu.gh"


# Build the border using string concatenation
border_part = "=========="
border = border_part + border_part + border_part + border_part

# Display student information
print()
print(border)
print("       STUDENT INFORMATION SYSTEM")
print(border)
print()
print("Full Name                  : " + full_name)
print("Student ID                 : " + student_id)
print("Programme                  : " + programme)
print("Level                      : " + level)
print("Age                        : " + age)
print("Favourite Language         : " + favourite_language)
print("Generated Username         : " + username)
print("Generated Email            : " + email)
profile_id = "UG-" + student_id + "-" + level
print("Student Profile ID         : " + profile_id)
print()
print(border)

# Part C Branch: Generate a unique student profile ID using string concatenation
print("Student Profile ID         : " + profile_id)
