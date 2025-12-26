import numpy as np

marks = np.random.randint(35, 100, size=(5, 4))
print("Marks:\n", marks)

# Averages
avg_student = np.average(marks, axis=1)
avg_subject = np.average(marks, axis=0)

print("Average per Student:", avg_student)
print("Average per Subject:", avg_subject)

# Failed students
failed_student = (marks < 45).any(axis=1)
failed_st = np.where(failed_student)[0]
print("Failed Students:", failed_st)

# Grace marks
mask = (marks >= 35) & (marks <= 49)
marks[mask] += 2

# New averages
new_avg = np.average(marks, axis=1)
print("New Average per Student:", new_avg)

# Passed students
passed_st = (marks >= 45).all(axis=1)
passed_indices = np.where(passed_st)[0]
print("Passed Students:", passed_indices)


