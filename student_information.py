full_name = input("Enter your full name: ")
student_id = input("Enter your student ID: ")
programme = input("Enter your programme: ")
level = input("Enter your level: ")
age = input("Enter your age: ")
favourite_language = input("Enter your favourite programming language: ")


# Generate student username and email using string concatenation
username = full_name[:3].lower() + student_id
email = username + "@st.ug.edu.gh"
