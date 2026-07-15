import numpy as np 
marks = np.array([50,60,70,80,90,100])

# you have to print the following things from the above array . 
# average marks.
# max marks 
# min marks 
# student above 80
# pass student #70%

print(f"Average marks: {np.average(marks)}")
print(f"Max marks: {np.max(marks)}")
print(f"Min marks: {np.min(marks)}")
print(f"student above 80 marks: {marks[marks > 80]}")
for x in np.nditer(np.where(marks>=70)):
    print(f"{x+1}-Pass")