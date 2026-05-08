# Assignment no 1
# Ultimate Student Profile System (Class Assignment)
# File Name: ultimate_student_profile.py

# Getting inputs for multiple students using for loop 
students = []
for i in range(2):
    stdNumber = i + 1
    stdName = input(f"Enter name for student {i+1}: ")
    stdAge = int(input(f"Enter age for student {i+1}:"))
    stdCity = input(f"Enter city for student {i+1}:")
    stdProfession = input(f"Enter profession for student {i+1}:")
    stdHeight = float(input(f"Enter height for student {i+1}:"))
    stdPyMarks = float(input(f"Enter python marks for student {i+1}:"))
    stdAiMarks = float(input(f"Enter ai marks for student {i+1}:"))
    stdData = [stdNumber,stdName, stdAge, stdCity, stdProfession, stdHeight, stdPyMarks, stdAiMarks]
    students.append(stdData)

for std in students:
    letsOfNameUsingLoop = ""
    for letter in std[1]:
        letsOfNameUsingLoop += letter + " "
    letsOfCityReverseUsingLoop = ""
    for letter in std[3][::-1]:
        letsOfCityReverseUsingLoop += letter + " "
    print(f"""
         --- Student {std[0]} ---
         First letter of name: {std[1][0]}
         Last letter of city: {std[3][-1]}
         Name reversed: {std[1][::-1]}
         First 3 letters of profession: {std[4][:3]}
         Every second letter of city: {std[3][::2]}
         Name capitalized: {std[1].capitalize()}
         Profession capitalized: {std[4].capitalize()}
         Length of name: {len(std[1])}
         Count of letter 'a' in name: {std[1].count('a')}
         Replace 'a' with '@' in name: {std[1].replace('a', '@')}
         Letters of name as list: {list(std[1])}
         Reversed letters of city as list: {list(std[3][::-1])}
         ...
         Total Marks: {std[6] + std[7]}
         Average Marks: {(std[6] + std[7]) / 2}
         Complex number: {complex(std[2],std[5])}
         Real part: {complex(std[2],std[5]).real}
         Imaginary part: {complex(std[2],std[5]).imag}
         Is age > 18? {std[2] > 18}
         Is python_marks == ai_marks? {std[6] == std[7]}
         Is 'a' in name? { 'a' in std[1] }
         Is 'z' not in name? { 'z' not in std[1] }
         Is name_list same as city_list? { list(std[1]) is list(std[3]) }
         Letters of name using loop: {letsOfNameUsingLoop}
         Letters of city reversed using loop: {letsOfCityReverseUsingLoop}
         ...
    """)

print("\t===== STUDENT SUMMARY =====")
for std in students:
    print(f"""
          {std[1]} \t \t Age+5: {std[2] + 5} Total: {std[6]+std[7]} Complex: {complex(std[2],std[5])}
    """)