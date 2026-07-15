# Sort the students based on their marks orderby lowest to highest using argsort.

import numpy as np

names = np.array(["Bilal","Hassan","Haroon","Wahaj","Ahmed"])
marks = np.array([76,91,25,45,16])

sorted_marks_index = np.argsort(marks)
sorted_names = names[sorted_marks_index]
print(sorted_names)
sorted_marks = marks[sorted_marks_index]
print(sorted_marks)
