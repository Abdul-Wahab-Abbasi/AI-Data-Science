import numpy as np
names = np.array(["Bilal","Hassan","Haroon","Wahaj","Ahmed"])
subjects = np.array(["Math","English","Physics","Urdu"])
marks = np.array([[76, 88, 65, 90],
                  [91, 72, 84, 68],
                  [25, 45, 38, 52],
                  [45, 60, 70, 55],
                  [16, 30, 42, 48]])

# *** Tasks ***
# 1. Print the shape and dimensions of the marks array
print("\n Task 1")
print(f"Dimensions of marks array: {marks.ndim} \nShape of marks array: {marks.shape}")

# 2. Total marks of each student (hint: axis=1)
print("\n Task 2")
student_totals = np.sum(marks,axis=1)
for name, total in zip(names, student_totals):
    print(f"Student {name} has scored total of {total} marks.")

# 3. Average marks of each subject (hint: axis=0)
print("\n Task 3")
subject_averages = np.mean(marks,axis=0)
for s_name, avg in zip(subjects, subject_averages):
    print(f"Average marks of {s_name} is:  {avg}")

# 4. Highest scorer in each subject — print the NAME, not the number
print("\n Task 4")
top_scorer_indexes =  np.argmax(marks,axis=0)
high_scorer_names = names[top_scorer_indexes]
for high_scorer, s_name, in zip(high_scorer_names, subjects):
    print(f"Highest scorer of {s_name} is:  {high_scorer}")


# 5. Rank all students from highest to lowest total
print("\n Task 5")
high_to_low_marks_indexes = np.argsort(student_totals)[::-1]
print(f"Students from Highest to Lowest: \n {names[high_to_low_marks_indexes]}")

# 6. Show only the students who scored above 80 in Math
print("\n Task 6")
score_above_80_math = marks[:,0] > 80
print(f"Students who scored above 80 in Math: {names[score_above_80_math]}")

# 7. Find students who failed (below 40) in ANY subject
print("\n Task 7")
below_40 = marks < 40
print(f"Students who failed (below 40) in ANY subject {names[np.any(below_40, axis=1)]}")

# 8. Give each student a grade: A (80+), B (60-79), C (40-59), F (below 40)
print("\n Task 8")
for name, total in zip(names,student_totals):
    print(f"\nGrade Book of {name}")
    total = round((total/400*100),2)
    if total >= 80:
        print(f"Percentage: {total}% | Grade: A")
    elif total >= 60:
        print(f"Percentage: {total}% | Grade: B")
    elif total >= 40:
        print(f"Percentage: {total}% | Grade: C")
    else:
        print(f"Percentage: {total}% | Grade:F")
