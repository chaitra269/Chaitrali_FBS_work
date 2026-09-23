# 2. WAP a menu driven program to perform following operations using
# files :

# a. Add a record
# b. Search for a record using id
# c. Delete a record using id
# d. Edit a record using id.
# e. Display all records.

import os
import pickle

# 1. Create a class Emp (eid, ename, basic)
class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def display(self):
        print(f"ID: {self.eid} | Name: {self.ename} | Basic Salary: {self.basic}")


FILENAME = "emp.dat"

# Helper function to load all records from file
def load_records():
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "rb") as f:
            return pickle.load(f)
    except EOFError:
        return []

# Helper function to save all records to file
def save_records(records):
    with open(FILENAME, "wb") as f:
        pickle.dump(records, f)


# a. Add a record
def add_record():
    records = load_records()
    eid = int(input("Enter Employee ID: "))
    
    # Check if ID already exists
    for emp in records:
        if emp.eid == eid:
            print("Error: Employee ID already exists!")
            return

    ename = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))
    
    emp = Emp(eid, ename, basic)
    records.append(emp)
    save_records(records)
    print("Record added successfully!")


# b. Search for a record using id
def search_record():
    records = load_records()
    if not records:
        print("No records found.")
        return
        
    search_eid = int(input("Enter Employee ID to search: "))
    found = False
    for emp in records:
        if emp.eid == search_eid:
            print("\nRecord Found:")
            emp.display()
            found = True
            break
    if not found:
        print("Record with given ID not found.")


# c. Delete a record using id
def delete_record():
    records = load_records()
    if not records:
        print("No records found.")
        return
        
    del_eid = int(input("Enter Employee ID to delete: "))
    updated_records = [emp for emp in records if emp.eid != del_eid]
    
    if len(updated_records) == len(records):
        print("Record with given ID not found.")
    else:
        save_records(updated_records)
        print("Record deleted successfully!")


# d. Edit a record using id
def edit_record():
    records = load_records()
    if not records:
        print("No records found.")
        return
        
    edit_eid = int(input("Enter Employee ID to edit: "))
    found = False
    
    for emp in records:
        if emp.eid == edit_eid:
            print("Current Details:")
            emp.display()
            emp.ename = input("Enter new Name (leave blank to keep same): ") or emp.ename
            new_basic = input("Enter new Basic Salary (leave blank to keep same): ")
            if new_basic:
                emp.basic = float(new_basic)
            found = True
            break
            
    if found:
        save_records(records)
        print("Record updated successfully!")
    else:
        print("Record with given ID not found.")


# e. Display all records
def display_all():
    records = load_records()
    if not records:
        print("No records found in the file.")
        return
        
    print("\n--- All Employee Records ---")
    for emp in records:
        emp.display()
    print("----------------------------")


# 2. Menu Driven Program
def main():
    while True:
        print("\n--- EMPLOYEE MANAGEMENT SYSTEM ---")
        print("a. Add a record")
        print("b. Search for a record using ID")
        print("c. Delete a record using ID")
        print("d. Edit a record using ID")
        print("e. Display all records")
        print("f. Exit")
        
        choice = input("Enter your choice (a-f): ").lower().strip()
        
        if choice == 'a':
            add_record()
        elif choice == 'b':
            search_record()
        elif choice == 'c':
            delete_record()
        elif choice == 'd':
            edit_record()
        elif choice == 'e':
            display_all()
        elif choice == 'f':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose between 'a' and 'f'.")

if __name__ == "__main__":
    main()
