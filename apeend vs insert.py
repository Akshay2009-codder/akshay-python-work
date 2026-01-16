import time
n = 100000
lst1 = []
start = time.time()
for i in range(n):
    lst1.append(i)
end = time.time()
print("Append time : ", end-start)


start = time.time()
lst2 = []
for i in range(n):
    lst2.insert(0,i)
end = time.time()
print("Insert at begining time :", end-start)
