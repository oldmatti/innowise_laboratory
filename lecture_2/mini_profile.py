def generate_profile(age):  
    if age >= 0 and age <= 12:
     return "Child"
    elif age >= 13 and age <= 19:
     return "Teenager"
    elif age >= 20:
     return "Adult"
    else:
        return "Unknown"

user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year

life_stage = generate_profile(current_age)

hobbies = []

while True:
    hobby_input = input("Enter hobby or type 'stop' to finish: ").strip()

    if hobby_input.lower() == "stop":
        break

    if hobby_input:
        hobbies.append(hobby_input)


user_profile = {
    "name": user_name,
    "age": current_age,
    "stage": life_stage,
    "hobbies": hobbies
}

print("\n---")
print("Profile Summary")
print(f"Name: {user_profile['name']}")
print(f"Age: {user_profile['age']}")
print(f"Life Stage: {user_profile['stage']}")

if not user_profile['hobbies']:
    print("You didn't mention any hobbies.")
else:

    count = len(user_profile['hobbies'])
    print(f"Favorite Hobbies ({count}):")
    for hobby in user_profile['hobbies']:
        print(f"- {hobby}")

print("---")