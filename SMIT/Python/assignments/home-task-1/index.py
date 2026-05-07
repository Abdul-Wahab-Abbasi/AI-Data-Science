print("="*50)
print("Student Management System".center(50))
print("="*50)
# creating menu
menu = {
    1: "All Students",
    2: "Search Student", 
    3: "Add Student", 
    4: "Update Student", 
    5: "Delete Student", 
    6: "Result System",
    }
# creating variable to store selected menu item
selectedMenu = ""

# dictionary to store students data
students = {
    1001: {
        "name": "ali raza",
        "marks": [85, 90, 78],
        "subjects": ("Math", "English", "Science")
    },

    1002: {
        "name": "sara khan",
        "marks": [88, 76, 95],
        "subjects": ("Physics", "Chemistry", "Biology")
    },

    1003: {
        "name": "hamza iqbal",
        "marks": [92, 81, 87],
        "subjects": ("Computer", "Math", "Statistics")
    }
}

# Main loop
while True:
    # loop for selecting menu item
    while True:
      print("\n"+"-"*20)
      print("Select Menu".center(20))
      print("-"*20)
      for item in menu:
          print(item, menu[item])
      userSelection = int(input("Enter menu number: "))
      if userSelection in menu:
          selectedMenu = menu[userSelection]
          break
    else:
        print("Invalid Selection, Please enter the number of available menu item")
        continue

    # showing all students
    if selectedMenu == 'All Students':
        print("\n"+"-"*20)
        print("All Students".center(20))
        print("-"*20)
        for std in students:
            print(f"Roll Number: {std}")
            print(f"Name: {students[std]['name'].title()}")
            print(f"Subjects: {', '.join(students[std]['subjects'])}")
            print(f"Marks: {', '.join(str(mark) for mark in students[std]['marks'])}")
            print("-"*20)
        print(f"Total Students: {len(students)}")

    # search students
    if selectedMenu == 'Search Student':
        print("\n"+"-"*20)
        print("Search Student".center(20))
        print("-"*20)
        # getting roll number to search
        searchRollNumber = int(input("Enter student roll number to search: "))
        # creating variable to check if student is found or not
        found = False
        for std in students:
            # checking if entered roll number matches with any student roll number
            if std == searchRollNumber:
                print(f"\nRoll Number: {std}")
                print(f"Name: {students[std]['name'].title()}")
                print(f"Subjects: {', '.join(students[std]['subjects'])}")
                print(f"Marks: {', '.join(str(mark) for mark in students[std]['marks'])}")
                print("-"*20)
                found = True
        if not found:
            print("Student not found.")
    
    # adding new student
    if selectedMenu == 'Add Student':
        print("\n"+"-"*20)
        print("Add Student".center(20))
        print("-"*20)
        # finding last roll number and adding 1 into it for new student roll number
        lastRollNumber = max(students.keys())
        newRollNumber = lastRollNumber + 1
        # using try except block to handle any error
        try:
            name = input("Enter student name: ")
            subjects = tuple(input("Enter subjects (comma separated): ").split(","))
            # creating empty list to store marks of subjects and using loop to get marks for each subject
            marks = []
            for subject in subjects:
                mark = int(input(f"Enter marks for {subject} (max: 100, min: 0): "))
                # checking if entered marks are greater than 100 or less than 0
                if mark > 100:
                    mark = 100
                if mark < 0:
                    mark = 0
                # appending marks into marks list
                marks.append(mark)
            # updating students dictionary with new student data
            students.update({
                newRollNumber: {
                    "name": name,
                    "subjects": subjects,
                    "marks": marks
                }
            })
            print("Student added successfully.")
        except:
            print("Something went wrong. Please enter the data in correct format.")
    if selectedMenu == 'Update Student':
        print("\n"+"-"*20)
        print("Update Student (Marks Or Name)".center(20))
        print("-"*20)
        # getting roll number to update
        updateRollNumber = int(input("Enter student roll number to update: "))
        # checking if entered roll number matches with any student roll number
        if updateRollNumber in students:
            # using try except block to handle any error
            try:
                name = input("Enter new student name: ")
                # same marks logic as add student
                marks = []
                for subject in students[updateRollNumber]["subjects"]:
                    mark = int(input(f"Enter new marks for {subject} (max: 100, min: 0): "))
                    if mark > 100:
                        mark = 100
                    if mark < 0:
                        mark = 0
                    marks.append(mark)
                # updating students dictionary with new student data
                students.update({
                    updateRollNumber: {
                        "name": name,
                        "subjects": students[updateRollNumber]["subjects"],
                        "marks": marks
                    }
                })
                print("Student updated successfully.")
            except:
                print("Something went wrong. Please enter the data in correct format.")
        else:
            print("Student not found.")
    if selectedMenu == 'Delete Student':
        print("\n"+"-"*20)
        print("Delete Student".center(20))
        print("-"*20)
        # getting roll number to delete
        deleteRollNumber = int(input("Enter student roll number to delete: "))
        # checking if entered roll number matches with any student roll number and deleting student if found
        if deleteRollNumber in students:
            students.pop(deleteRollNumber)
            print("Student deleted successfully.")
        else:
            print("Student not found.")
    # showing result system
    if selectedMenu == 'Result System':
        print("\n"+"-"*20)
        print("Result System".center(20))
        print("-"*20)
        # creating variable to store topper roll number and topper percentage
        topper = 0
        topper_percentage = 0
        for std in students:
            # calculating percentage and grade for each student
            obtainedMarks = sum(students[std]['marks'])
            totalMarks = 100 * len(students[std]['subjects'])
            percentage = (obtainedMarks / totalMarks) * 100
            if percentage >= 90:
                grade = "A"
            elif percentage >= 80:
                grade = "B"
            elif percentage >= 70:
                grade = "C"
            elif percentage >= 60:
                grade = "D"
            else:
                grade = "F"
            print(f"Roll Number: {std}")
            print(f"Name: {students[std]['name'].title()}")
            print(f"Total Marks: {totalMarks}")
            print(f"Percentage: {round(percentage,2)}%")
            print(f"Grade: {grade}")
            print("-"*20)
            # finding topper
            if percentage > topper_percentage:
                topper = std
                topper_percentage = percentage
        # showing topper
        print(f"Topper: {students[topper]['name'].title()} with {round(topper_percentage,2)}%")