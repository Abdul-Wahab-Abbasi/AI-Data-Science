# Assignment no 2
# Ultimate Hackathon: Multi-Student AI & Ranking System
# File Name: ultimate_hackathon.py

# Getting inputs for multiple students using loop
students = []
sortedStudents = []
num_students = int(input("Enter number of students: "))
best_python_student = 0
for i in range(num_students):
    stdNumber = i + 1
    stdName = input(f"Enter name for student {i+1}: ")
    stdAge = int(input(f"Enter age for student {i+1}:"))
    stdCity = input(f"Enter city for student {i+1}:")
    stdPyMarks = float(input(f"Enter python marks for student {i+1}:"))
    stdAiMarks = float(input(f"Enter ai marks for student {i+1}:"))
    stdEngMarks = float(input(f"Enter english marks for student {i+1}:"))
    stdTech = input(f"Enter favourite technology for student {i+1}:")
    stdHeight = float(input(f"Enter height for student {i+1}:"))
    total_marks = stdPyMarks + stdAiMarks + stdEngMarks
    stdData = [stdNumber,stdName, stdAge, stdCity, stdPyMarks, stdAiMarks, stdEngMarks, stdTech, stdHeight, total_marks]
    students.append(stdData)
    if(i > 0 and total_marks > students[i-1][-1]):
        sortedStudents.append(stdData)
    else:
        sortedStudents.insert(i-1, stdData)
        
    if (i > 0 and stdPyMarks>students[i-1][4]):
        best_python_student = i

for std in students:
    total_marks = std[-1]
    average_marks = total_marks / 3
    complex_num = complex(std[4], std[5])
    print(f"""
         --- Student {std[0]} ---
         Name in uppercase: {std[1].upper()}
         City reversed: {std[3][::-1]}
         Every second letter of name: {std[1][::2]}
         Technology capitalized: {std[7].capitalize()}
         Length of name: {len(std[1])}
         Count of letter 'a' in name: {std[1].count('a')}
         Find 'e' in city: {std[3].find('e')}
         Replace 'a' with '@' in technology: {std[7].replace('a', '@')}
         Total Marks: {total_marks}
         Average Marks: {average_marks}
         Complex number (Python + AI): {complex_num}
         Is python marks > 50 AND < 100? {50 < std[4] < 100}
         Letter of name: {list(std[1])}    
         Letter of technology: {list(std[7])}    
         Name reversed using list: {list(std[1][::-1])}    
         Technology reversed using list: {list(std[7][::-1])}    
    """)
# summary table
print("\t===== STUDENT SUMMARY =====")
print("Name\tTotal\tAverage\tComplex\tTechnology")
sortedStudents.reverse()
for std in sortedStudents:
    total_marks = std[-1]
    average_marks = total_marks / 3
    complex_num = complex(std[4], std[5])
    print(f"{std[1]}\t{total_marks}\t{average_marks:.2f}\t{complex_num}\t{std[7]}")


print(f"Top Student Overall: {sortedStudents[0][1]} with total marks: {sortedStudents[0][-1]}")
print(f"Best Python Marks Student: {students[best_python_student][1]} with marks: {students[best_python_student][4]}")