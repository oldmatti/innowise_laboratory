import sys
from functools import reduce

# 1. Student Data (The Starting Point)
students = []


def calculate_average(grades):
    """Calculates the average of a list of grades, handling empty lists (ZeroDivisionError)."""
    try:
        # Using a simple check to avoid reduce on empty list, though reduce handles it if initial value is set,
        # the requirement is to handle ZeroDivisionError (which occurs if summing an empty list and dividing by 0).
        if not grades:
            raise ZeroDivisionError

        total = sum(grades)
        return total / len(grades)
    except ZeroDivisionError:
        return "N/A"
    except TypeError:
        # Handles cases where grades might contain non-numbers (although input logic should prevent this)
        return "Error"


def find_student(name):
    """Finds a student dictionary in the students list by name (case-insensitive)."""
    for student in students:
        if student['name'].lower() == name.lower():
            return student
    return None


def display_menu():
    """Displays the main menu options."""
    print("\n--- Student Grade Analyzer ---")
    print("1. Add a new student")
    print("2. Add grades for a student")
    print("3. Generate a full report")
    print("4. Find top performer")
    print("5. Exit program")
    print("------------------------------")


# --- Menu Options Implementation ---

# Option 1: Add a new student
def add_new_student():
    """Handles adding a new student to the global students list."""
    student_name = input("Enter student name: ")

    if find_student(student_name):
        print(f"Error: Student '{student_name}' already exists.")
        return

    # Create a new dictionary with keys 'name' and 'grades'
    new_student = {
        'name': student_name,
        'grades': []  # 'grades' value should be an empty list
    }
    students.append(new_student)
    print(f"Student '{student_name}' added successfully.")


# Option 2: Add a grade for a student
def add_grades_for_student():
    """Handles adding grades for an existing student."""
    student_name = input("Enter student name: ")
    student = find_student(student_name)

    if not student:
        print(f"Error: Student '{student_name}' not found.")
        return

    print(f"Adding grades for {student_name}. Enter a grade (or 'done' to finish):")

    while True:
        grade_input = input("Enter a grade (or 'done' to finish): ").strip()

        if grade_input.lower() == 'done':
            break

        try:
            grade = float(grade_input)

            # Check for valid range [0, 100]
            if 0 <= grade <= 100:
                # Add the grade to the student's list of grades
                student['grades'].append(grade)
            else:
                print("Invalid grade. Grade must be between 0 and 100.")
        except ValueError:
            # Handling potential errors (e.g., input like 'banana')
            print("Invalid input. Please enter a valid number or 'done'.")


# Option 3: Show report (all students)
def generate_report():
    """Generates and prints a full report including student averages and overall statistics."""

    if not students:
        print("No students added yet. Please add students first.")
        return

    print("--- Student Report ---")

    all_averages = []

    # Iterate through students and calculate individual averages
    for student in students:
        avg = calculate_average(student['grades'])

        # Print message like: "[Student's name]'s average grade is [average]."
        print(f"{student['name']}'s average grade is {avg}.")

        # Collect numerical averages for overall statistics, skipping 'N/A'
        if isinstance(avg, (int, float)):
            all_averages.append(avg)

    print("-" * 20)

    # Calculate overall statistics
    if not all_averages:
        print("No overall averages available (no students have grades).")
    else:
        # Max Average
        max_avg = max(all_averages)
        # Min Average
        min_avg = min(all_averages)
        # Overall Average (Total of all averages divided by number of students with grades)
        overall_avg = sum(all_averages) / len(all_averages)

        print(f"Max Average: {max_avg}")
        print(f"Min Average: {min_avg}")
        print(f"Overall Average: {overall_avg:.1f}")  # Format to one decimal place


# Option 4: Find top performer
def find_top_performer():
    """Finds and reports the student with the highest average grade."""

    if not students:
        print("No students added yet. Cannot find top performer.")
        return

    # Filter students who have grades (average is a number)
    students_with_grades = [
        student for student in students
        if isinstance(calculate_average(student['grades']), (int, float))
    ]

    if not students_with_grades:
        print("No students have grades yet. Cannot find top performer.")
        return

    # Use max() with a lambda function as the key
    # The lambda returns the average grade for the student dictionary
    top_student = max(
        students_with_grades,
        key=lambda student: calculate_average(student['grades'])
    )

    top_avg = calculate_average(top_student['grades'])

    # Print clear message showing the name of the top student
    print(f"The student with the highest average is {top_student['name']} with a grade of {top_avg}.")


# --- Main Program Loop ---

def run_analyzer():
    """The main entry point for the Student Grade Analyzer program."""
    while True:
        display_menu()

        # Use try/except block to handle potential input errors for choice
        try:
            choice = input("Enter your choice: ")

            if choice == '1':
                add_new_student()
            elif choice == '2':
                add_grades_for_student()
            elif choice == '3':
                generate_report()
            elif choice == '4':
                find_top_performer()
            elif choice == '5':
                print("Exiting program.")
                sys.exit()  # Option 5: Exit program (Break the infinite loop)
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

        except EOFError:  # Handles Ctrl+D/Ctrl+Z input
            print("\nExiting program due to interrupt.")
            sys.exit()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    run_analyzer()