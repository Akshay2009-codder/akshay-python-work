import os

print(os.getcwd())          #ye meri current directory kya hai vo batata hai
os.chdir("c://")           #ye hamari directory change karta hain
print(os.getcwd())

print(os.listdir())        #ye jis directory me jtni files hai unko return karta hain

# os.mkdir("folder ka name ")   # ye os.mkdir new folder banati hai

print(os.path.join("c/","Akshay.txt"))