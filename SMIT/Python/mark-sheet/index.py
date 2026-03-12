stdName = input("Enter Student Name: ");
stdRoll = input("Enter Student Roll No: ");
engMarks = float(input("Enter English Marks: "));
urduMarks = float(input("Enter Urdu Marks: "));
mathMarks = float(input("Enter Math Marks: "));
totalMarks = engMarks + urduMarks + mathMarks;
percentage = (totalMarks / 300) * 100;
print(f"""Student Name: {stdName}
Student Roll No: {stdRoll}
English Marks: {engMarks}
Urdu Marks: {urduMarks}
Math Marks: {mathMarks}
Total Marks: {totalMarks}
Percentage: {round(percentage,2)}%
""")