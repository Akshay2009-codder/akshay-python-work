import pickle
# pickel function ek esa function hai jo item ko file me pickel karta hai

"""names = ["yash","rudra","sahal","farhan","pikachu"]
file = "names.pickle"
fileobj = open(file, "wb")
pickle.dump(names, fileobj)
fileobj.close()"""

# pahle hamne ek pickel file me list  save kari bainory format me

# baad me usko load kia

"""file = "names.pickle"
fileobj = open(file, "rb")
names = pickle.load(fileobj)
print(names)
fileobj.close()"""