import numpy as np

marks = np.random.randint(35,100, size=(5,6))

avg_st = np.round(np.average(marks, axis=1), 2)
avg_sub = np.round(np.average(marks, axis=0), 2)
top_st = np.max(marks, axis=1)
st_max_index = np.argmax(top_st)
st_min_index = np.argmin(top_st)


print("Average marks per student : ", avg_st)
print("Average marks per subject : ", avg_sub)
print("Max student index : ", st_max_index)
print("Min student index : ", st_min_index)

failed_st = (marks<40).any (axis=1)
fail_mask = marks<40
adding = fail_mask.sum(axis=1)




