import csv
import os

FILENAME = "student_records.csv"

def load_data():
    """Loads student records from a CSV file into a dictionary."""
    records = {}
    if not os.path.exists(FILENAME):
        return records
    try:
        with open(FILENAME, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                records[row['ID']] = {
                    'Name': row['Name'],
                    'Age': int(row['Age']),
                    'Marks': float(row['Marks']),
                    'Subject': row['Subject']
                }
    except Exception as e:
        print(f"Error loading records: {e}")
    return records

def save_data(records):
    """Saves the current dictionary of student records back to the CSV file."""
    try:
        with open(FILENAME, mode='w', newline='') as file:
            fieldnames = ['ID', 'Name', 'Age', 'Marks', 'Subject']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for stud_id, info in records.items():
                writer.writerow({
                    'ID': stud_id,
                    'Name': info['Name'],
                    'Age': info['Age'],
                    'Marks': info['Marks'],
                    'Subject': info['Subject']
                })
    except Exception as e:
        print(f"Error saving records: {e}")

def add_student(records):
    stud_id = input("Enter Student ID (Unique): ").strip()
    if stud_id in records:
        print("❌ Error: A student with this ID already exists.")
        return
    
    try:
        name = input("Enter Student Name: ").strip()
        age = int(input("Enter Student Age: "))
        subject = input("Enter Primary Subject: ").strip()
        marks = float(input("Enter Marks Obtained: "))
        
        records[stud_id] = {'Name': name, 'Age': age, 'Marks': marks, 'Subject': subject}
        save_data(records)
        print("✅ Student record added successfully!")
    except ValueError:
        print("❌ Invalid input type. Age must be an integer, and Marks must be a number.")

def view_students(records):
    if not records:
        print("ℹ️ No records found.")
        return
    print("\n--- Student Records ---")
    print(f"{'ID':<10} {'Name':<20} {'Age':<6} {'Subject':<15} {'Marks':<6}")
    print("-" * 60)
    for stud_id, info in records.items():
        print(f"{stud_id:<10} {info['Name']:<20} {info['Age']:<6} {info['Subject']:<15} {info['Marks']:<6.2f}")

def update_student(records):
    stud_id = input("Enter the Student ID to update: ").strip()
    if stud_id not in records:
        print("❌ Student record not found.")
        return
    
    print("Leave field blank to keep current value.")
    try:
        name = input(f"New Name ({records[stud_id]['Name']}): ").strip() or records[stud_id]['Name']
        age_input = input(f"New Age ({records[stud_id]['Age']}): ").strip()
        age = int(age_input) if age_input else records[stud_id]['Age']
        subject = input(f"New Subject ({records[stud_id]['Subject']}): ").strip() or records[stud_id]['Subject']
        marks_input = input(f"New Marks ({records[stud_id]['Marks']}): ").strip()
        marks = float(marks_input) if marks_input else records[stud_id]['Marks']
        
        records[stud_id] = {'Name': name, 'Age': age, 'Marks': marks, 'Subject': subject}
        save_data(records)
        print("✅ Student record updated successfully!")
    except ValueError:
        print("❌ Invalid input formatting. Updates aborted.")

def delete_student(records):
    stud_id = input("Enter the Student ID to delete: ").strip()
    if stud_id in records:
        del records[stud_id]
        save_data(records)
        print("✅ Student record deleted successfully!")
    else:
        print("❌ Student record not found.")

def main():
    records = load_data()
    while True:
        print("\n=== Student Record Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ").strip()
        if choice == '1':
            add_student(records)
        elif choice == '2':
            view_students(records)
        elif choice == '3':
            update_student(records)
        elif choice == '4':
            delete_student(records)
        elif choice == '5':
            print("Exiting system. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please pick between 1 and 5.")

if __name__ == "__main__":
    main()
