import numpy as np

marks = np.random.randint(1,100, size = (4,5))

avg_student = np.average(marks, axis = 0)
avg_subject = np.average(marks, axis = 1)
st_total = np.sum(marks, axis = 1)
top_score = max(st_total)
